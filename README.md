# Village Grievance Redressal System (VGRS)

## Project Overview
The Village Grievance Redressal System (VGRS) is a web application built with Flask that allows users to register, submit complaints related to various categories, track the status of their complaints, and communicate with administrators. The system also provides an admin dashboard for managing and updating complaints.

## Features
- User registration and login with secure password hashing
- Password reset via token-based email link
- Complaint submission with optional photo upload
- Complaint tracking by complaint ID or user
- Admin dashboard with complaint management and status updates
- Role-based access control for users and admins
- Contact page for general inquiries

## Technologies Used
- Python 3
- Flask
- Flask-Login
- Flask-SQLAlchemy
- Werkzeug (for password hashing and secure file uploads)
- SQLite (database)
- HTML, CSS, JavaScript (frontend templates and static files)

## Setup Instructions
1. Clone the repository or download the source code.
2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   venv\Scripts\activate   # On Windows
   source venv/bin/activate  # On macOS/Linux
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Initialize the database:
   ```bash
   python init_db.py
   ```
5. Run the Flask application:
   ```bash
   python app.py
   ```
6. Open your browser and navigate to `http://127.0.0.1:5000/` to access the application.

## Usage
- Register a new user account or login with existing credentials.
- Submit complaints by selecting a category, providing a description, and optionally uploading a photo.
- Track your complaints using the complaint ID or view all your complaints.
- Admin users can log in to the admin dashboard to view and update complaint statuses and add remarks.
- Use the contact page for any general inquiries.

## File Structure
- `app.py`: Main Flask application with route definitions and application logic.
- `models.py`: Database models for User and Complaint.
- `init_db.py`: Script to initialize the database schema.
- `templates/`: HTML templates for rendering pages.
- `static/`: Static files including CSS, JavaScript, and uploaded photos.
- `instance/vgrs.db`: SQLite database file (created after initialization).
- `requirements.txt`: Python dependencies list.

## License
This project is licensed under the MIT License.
