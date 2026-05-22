# Village Grievance Redressal System (VGRS)

## Project Overview
The Village Grievance Redressal System (VGRS) is a web application built with Flask that allows users to register, submit complaints related to various categories, track the status of their complaints, and receive updates. The system provides an efficient and transparent mechanism for handling grievances at the village level.

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

## Prerequisites
Before you begin, ensure you have the following installed:
- Python 3.7 or higher
- pip (Python package manager)
- Virtual environment support
- Modern web browser (Chrome, Firefox, Safari, Edge)

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
- **User Registration**: Register a new user account with email and password
- **Login**: Access your account using registered credentials
- **Submit Complaints**: Select category, provide description, and optionally upload photos
- **Track Complaints**: Monitor status using complaint ID or view all your submissions
- **Admin Dashboard**: Admins can view, update status, and add remarks to complaints
- **Contact Support**: Use the contact page for general inquiries

## File Structure
```
village-grivenace-redressal-system/
├── app.py                 # Main Flask application with route definitions
├── models.py              # Database models for User and Complaint
├── init_db.py             # Database initialization script
├── requirements.txt       # Python dependencies
├── templates/             # HTML templates
│   ├── index.html
│   ├── register.html
│   ├── login.html
│   ├── submit_complaint.html
│   ├── track_complaint.html
│   ├── admin_dashboard.html
│   └── contact.html
├── static/                # Static files
│   ├── css/               # Stylesheets
│   ├── js/                # JavaScript files
│   └── uploads/           # User uploaded photos
└── instance/
    └── vgrs.db            # SQLite database file
```

## Database Schema

### User Table
- `id`: Primary key
- `username`: User's username (unique)
- `email`: User's email (unique)
- `password`: Hashed password
- `is_admin`: Boolean flag for admin privileges
- `created_at`: Account creation timestamp

### Complaint Table
- `id`: Primary key (complaint ID)
- `user_id`: Foreign key to User table
- `category`: Complaint category
- `description`: Detailed complaint description
- `photo_path`: Path to uploaded photo (optional)
- `status`: Current status (Pending/Under Review/Resolved/Rejected)
- `remarks`: Admin remarks
- `created_at`: Submission timestamp
- `updated_at`: Last update timestamp

## Configuration
The application uses default Flask configuration. To customize:
- Edit Flask settings in `app.py` (debug mode, port, etc.)
- Database location can be changed in the connection string
- Upload folder path can be modified in `app.py`

## API Endpoints

### User Routes
- `GET /` - Home page
- `GET/POST /register` - User registration
- `GET/POST /login` - User login
- `GET /logout` - User logout

### Complaint Routes
- `GET/POST /submit_complaint` - Submit new complaint
- `GET /track_complaint` - Track complaint by ID
- `GET /my_complaints` - View all user complaints

### Admin Routes
- `GET /admin_dashboard` - Admin dashboard
- `GET/POST /admin_dashboard/<complaint_id>` - Update complaint status

### Support Routes
- `GET/POST /contact` - Contact/Support page

## Troubleshooting

**Issue: Database not found**
- Solution: Run `python init_db.py` to initialize the database

**Issue: Port 5000 already in use**
- Solution: Change the port in `app.py` or stop the process using port 5000

**Issue: Photo upload not working**
- Solution: Ensure `static/uploads/` directory exists with proper permissions

**Issue: Password reset email not received**
- Solution: Configure your email settings in `app.py` and ensure SMTP credentials are correct

**Issue: Admin login not working**
- Solution: Ensure the user account is marked as admin in the database

## Security Notes
⚠️ **Important for Production Deployment:**
- Change Flask secret key in `app.py` to a strong, random value
- Use environment variables for sensitive credentials (database URL, email, etc.)
- Enable HTTPS/SSL in production
- Set secure cookie flags in Flask configuration
- Implement rate limiting for login attempts
- Regularly backup the database
- Validate and sanitize all user inputs
- Keep dependencies updated with security patches

## Contributing
Contributions are welcome! To contribute:
1. Fork the repository
2. Create a new branch for your feature (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Project Status
- ✅ Active Development
- 🎯 Core features complete
- 📋 Looking for contributors
- 🔄 Continuous improvements welcome

## Contact & Support
For questions, suggestions, or issues:
- Email: balamanikanta2942005@gmail.com
- GitHub Issues: [Create an issue](https://github.com/BALAMANIKANTA29/village-grivenace-redressal-system/issues)

## Author
**Bala Manikanta Naradala**
- GitHub: [@BALAMANIKANTA29](https://github.com/BALAMANIKANTA29)

---

*Last Updated: May 2026*
