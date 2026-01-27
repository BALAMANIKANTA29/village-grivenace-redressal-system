from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime

db = SQLAlchemy()

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    role = db.Column(db.String(20), default='Citizen')  # 'Citizen' or 'Officer'
    department = db.Column(db.String(100))  # For Officers
    assigned_district = db.Column(db.String(100))  # For Officers
    assigned_mandal = db.Column(db.String(100))  # For Officers
    reset_token = db.Column(db.String(100), nullable=True)
    reset_token_expiry = db.Column(db.DateTime, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    complaints = db.relationship('Complaint', backref='user', lazy=True)

class Complaint(db.Model):
    __tablename__ = 'complaints'
    complaint_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    department = db.Column(db.String(100))  # Auto-assigned based on category
    description = db.Column(db.Text, nullable=False)
    
    # Location Details
    state = db.Column(db.String(100), default='Andhra Pradesh') # Default or selected
    district = db.Column(db.String(100), nullable=False)
    mandal = db.Column(db.String(100), nullable=False)
    ward = db.Column(db.String(100))
    
    photo = db.Column(db.String(200))  # Path to uploaded photo
    status = db.Column(db.String(20), default='Submitted')  # Submitted, In Progress, Resolved, Rejected
    officer_remarks = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
