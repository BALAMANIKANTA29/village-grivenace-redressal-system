# VGRS Flask Application
from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
import os
import secrets
from datetime import datetime, timedelta
from models import db, User, Complaint

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///vgrs.db'
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# Category to Department Mapping
CATEGORY_MAPPING = {
    'Public Services': 'General Administration',
    'Infrastructure & Development': 'Infrastructure Dept',
    'Health & Medical Services': 'Health Dept',
    'Education': 'Education Dept',
    'Revenue & Land': 'Revenue Dept',
    'Law & Order / Public Safety': 'Police Dept',
    'Employment & Welfare Schemes': 'Employment Dept',
    'Banking & Financial Services': 'Finance Dept',
    'Social Welfare': 'Social Welfare Dept',
    'Housing & Urban Development': 'Housing Dept',
    'Agriculture & Environment': 'Agriculture Dept',
    'Transport': 'Transport Dept',
    'Documentation & Certificates': 'Revenue Dept',
    'Others': 'General Administration'
}

db.init_app(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Ensure upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        email = request.form['email']
        password = request.form['password']
        is_admin = 'is_admin' in request.form

        if User.query.filter_by(email=email).first():
            flash('Email already registered')
            return redirect(url_for('register'))

        hashed_password = generate_password_hash(password)
        new_user = User(name=name, phone=phone, email=email, password=hashed_password, is_admin=is_admin)
        db.session.add(new_user)
        db.session.commit()

        flash('Registration successful')
        return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            if user.role == 'Officer':
                return redirect(url_for('officer_dashboard'))
            return redirect(url_for('home'))
        else:
            flash('Invalid email or password')

    return render_template('login.html')

@app.route('/forgot_password', methods=['GET', 'POST'])
def forgot_password():
    if request.method == 'POST':
        email = request.form.get('email')
        user = User.query.filter_by(email=email).first()
        if user:
            token = secrets.token_urlsafe(32)
            expiry = datetime.utcnow() + timedelta(hours=1)
            user.reset_token = token
            user.reset_token_expiry = expiry
            db.session.commit()
            reset_url = url_for('reset_password', token=token, _external=True)
            flash(f'Password reset link: {reset_url}')
        else:
            flash('Email not found')
    return render_template('forgot_password.html')

@app.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    user = User.query.filter_by(reset_token=token).first()
    if not user or user.reset_token_expiry < datetime.utcnow():
        flash('Invalid or expired token')
        return redirect(url_for('login'))

    if request.method == 'POST':
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        if password != confirm_password:
            flash('Passwords do not match')
            return render_template('reset_password.html')
        user.password = generate_password_hash(password)
        user.reset_token = None
        user.reset_token_expiry = None
        db.session.commit()
        flash('Password reset successfully')
        return redirect(url_for('login'))

    return render_template('reset_password.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/submit_complaint', methods=['GET', 'POST'])
@login_required
def submit_complaint():
    if request.method == 'POST':
        category = request.form['category']
        description = request.form['description']
        photo = request.files.get('photo')

        if photo and photo.filename:
            filename = secure_filename(photo.filename)
            photo_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            photo.save(photo_path)

        # Auto-assign department
        department = CATEGORY_MAPPING.get(category, 'General Administration')
        
        # Get location details
        district = request.form['district']
        mandal = request.form['mandal']
        ward = request.form.get('ward', '')

        new_complaint = Complaint(
            user_id=current_user.id,
            category=category,
            department=department,
            description=description,
            district=district,
            mandal=mandal,
            ward=ward,
            photo=photo_path,
            status='Submitted'
        )
        db.session.add(new_complaint)
        db.session.commit()

        flash('Complaint submitted successfully')
        return redirect(url_for('track_complaint'))

    return render_template('submit_complaint.html')

@app.route('/track_complaint', methods=['GET', 'POST'])
@login_required
def track_complaint():
    complaints = None
    if request.method == 'POST':
        complaint_id = request.form.get('complaint_id')
        if complaint_id:
            complaints = Complaint.query.filter_by(complaint_id=complaint_id, user_id=current_user.id).all()
        else:
            complaints = Complaint.query.filter_by(user_id=current_user.id).all()
    else:
        complaints = Complaint.query.filter_by(user_id=current_user.id).all()

    return render_template('track_complaint.html', complaints=complaints)

@app.route('/admin_dashboard')
@login_required
def admin_dashboard():
    admin_password = "12345678"  # Updated admin password as requested

    if not current_user.is_admin:
        flash('Access denied')
        return redirect(url_for('home'))

    # Additional password check for admin access
    if 'admin_password' not in session or session['admin_password'] != admin_password:
        flash('Please enter admin password to access this page')
        return redirect(url_for('admin_login'))

    complaints = Complaint.query.all()
    return render_template('admin_dashboard.html', complaints=complaints)

@app.route('/officer_dashboard')
@login_required
def officer_dashboard():
    if current_user.role != 'Officer':
        flash('Access denied. Officer privileges required.')
        return redirect(url_for('home'))

    # Filter by Department and District
    query = Complaint.query.filter_by(
        department=current_user.department, 
        district=current_user.assigned_district
    )
    
    # If officer is assigned to specific mandal, filter by it too
    if current_user.assigned_mandal:
        query = query.filter_by(mandal=current_user.assigned_mandal)
        
    complaints = query.all()
    return render_template('officer_dashboard.html', complaints=complaints)

@app.route('/admin_login', methods=['GET', 'POST'])
@login_required
def admin_login():
    if not current_user.is_admin:
        flash('Access denied')
        return redirect(url_for('home'))

    if request.method == 'POST':
        password = request.form.get('password')
        admin_password = "12345678"  # Updated admin password as requested

        if password == admin_password:
            session['admin_password'] = password
            return redirect(url_for('admin_dashboard'))
        else:
            flash('Invalid admin password')

    return render_template('admin_login.html')

@app.route('/update_complaint/<int:complaint_id>', methods=['POST'])
@login_required
def update_complaint(complaint_id):
    # Allow Admin or Officer
    if not current_user.is_admin and current_user.role != 'Officer':
        flash('Access denied')
        return redirect(url_for('home'))

    complaint = Complaint.query.get_or_404(complaint_id)
    status = request.form['status']
    remarks = request.form.get('remarks', '')

    complaint.status = status
    complaint.officer_remarks = remarks
    db.session.commit()

    flash('Complaint updated successfully')
    if current_user.role == 'Officer':
        return redirect(url_for('officer_dashboard'))
    return redirect(url_for('admin_dashboard'))

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
