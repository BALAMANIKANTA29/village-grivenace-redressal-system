from app import app
from models import db, User
from werkzeug.security import generate_password_hash

def seed_data():
    with app.app_context():
        print("dropping old db...")
        db.drop_all()
        print("Creating tables...")
        db.create_all()

        print("Seeding users...")
        # Admin
        admin = User(
            name='System Administrator',
            phone='9999999999',
            email='admin@govt.in',
            password=generate_password_hash('admin123'),
            is_admin=True,
            role='Admin'
        )

        # Officers
        # 1. Health Officer - Visakhapatnam
        off_health_vizag = User(
            name='Dr. Ramesh (Health Officer)',
            phone='9876543210',
            email='health_vizag@govt.in',
            password=generate_password_hash('officer123'),
            role='Officer',
            department='Health Dept',
            assigned_district='Visakhapatnam'
        )
        
        # 2. Police Officer - Visakhapatnam
        off_police_vizag = User(
            name='ACP Kishore (Police)',
            phone='8888888888',
            email='police_vizag@govt.in',
            password=generate_password_hash('officer123'),
            role='Officer',
            department='Police Dept',
            assigned_district='Visakhapatnam'
        )

        # 3. Revenue Officer - Guntur
        off_revenue_guntur = User(
            name='MRO Krishna (Revenue)',
            phone='7777777777',
            email='revenue_guntur@govt.in',
            password=generate_password_hash('officer123'),
            role='Officer',
            department='Revenue Dept',
            assigned_district='Guntur'
        )

        # Citizen
        citizen = User(
            name='Raju Citizen',
            phone='9000000000',
            email='citizen@gmail.com',
            password=generate_password_hash('citizen123'),
            role='Citizen'
        )

        db.session.add_all([admin, off_health_vizag, off_police_vizag, off_revenue_guntur, citizen])
        db.session.commit()
        print("Database seeded successfully!")
        print("Credentials:")
        print("Admin: admin@govt.in / admin123")
        print("Officer (Health Vizag): health_vizag@govt.in / officer123")
        print("Officer (Police Vizag): police_vizag@govt.in / officer123")
        print("Citizen: citizen@gmail.com / citizen123")

if __name__ == '__main__':
    seed_data()
