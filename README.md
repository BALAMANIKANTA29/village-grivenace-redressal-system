# Village Grievance Redressal System (VGRS)

## Project Overview
The Village Grievance Redressal System (VGRS) is a comprehensive web application built with Flask that enables citizens to register complaints, track their resolution status, and communicate with government officials. The system features a multi-tier role-based architecture with separate dashboards for Citizens, Officers, and Administrators, ensuring efficient complaint management and resolution at the village/mandal level.

## Features

### User Management
- **Multi-Role System**: Support for three user roles:
  - **Citizens**: Can submit and track complaints
  - **Officers**: Department-specific officials who manage complaints in their assigned areas
  - **Admins**: Full system access with complaint oversight capabilities
- **Secure Authentication**: User registration and login with password hashing using Werkzeug
- **Password Recovery**: Token-based password reset functionality with email link generation
- **Profile Management**: User profiles with contact information and role-specific details

### Complaint Management
- **Complaint Submission**: 
  - 14 predefined complaint categories covering all government services
  - Optional photo upload support (up to 16MB)
  - Location tracking (State, District, Mandal, Ward)
  - Automatic department assignment based on complaint category
- **Complaint Tracking**: 
  - Track complaints by unique complaint ID
  - View all personal complaints with status updates
  - Real-time status monitoring (Submitted, In Progress, Resolved, Rejected)
- **Location-Based Filtering**: Complaints are automatically routed to officers based on district and mandal assignments

### Department & Category Mapping
Automatic department assignment for 14 complaint categories:
- Public Services → General Administration
- Infrastructure & Development → Infrastructure Dept
- Health & Medical Services → Health Dept
- Education → Education Dept
- Revenue & Land → Revenue Dept
- Law & Order / Public Safety → Police Dept
- Employment & Welfare Schemes → Employment Dept
- Banking & Financial Services → Finance Dept
- Social Welfare → Social Welfare Dept
- Housing & Urban Development → Housing Dept
- Agriculture & Environment → Agriculture Dept
- Transport → Transport Dept
- Documentation & Certificates → Revenue Dept
- Others → General Administration

### Officer Dashboard
- **Department-Specific Access**: Officers only see complaints assigned to their department
- **Location-Based Filtering**: Complaints filtered by assigned district and mandal
- **Complaint Management**: Update complaint status and add officer remarks
- **Status Updates**: Change complaint status (In Progress, Resolved, Rejected)

### Admin Dashboard
- **Full System Access**: View and manage all complaints across all departments
- **Two-Factor Security**: Additional password verification for admin access
- **Comprehensive Overview**: Monitor all complaints, users, and system activity
- **Complaint Updates**: Update any complaint status and add administrative remarks

### Additional Features
- **Contact Page**: General inquiries and support information
- **Responsive Design**: Mobile-friendly interface
- **File Upload Security**: Secure filename handling and file size restrictions
- **Session Management**: Secure session handling with Flask-Login
- **Database Relationships**: Proper foreign key relationships between users and complaints

## Technologies Used
- **Backend**: Python 3, Flask
- **Authentication**: Flask-Login
- **Database**: Flask-SQLAlchemy with SQLite
- **Security**: Werkzeug (password hashing, secure file uploads)
- **Frontend**: HTML5, CSS3, JavaScript
- **File Handling**: Werkzeug secure filename utilities

## Setup Instructions

### 1. Clone the Repository
```bash
git clone <repository-url>
cd vgrs
```

### 2. Create Virtual Environment
```bash
# On Windows
python -m venv .venv
.venv\Scripts\activate

# On macOS/Linux
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Initialize the Database
```bash
python init_db.py
```

### 5. (Optional) Seed Sample Data
```bash
python seed.py
```

### 6. Run the Application
```bash
python app.py
```

### 7. Access the Application
Open your browser and navigate to: `http://127.0.0.1:5000/`

## Usage Guide

### For Citizens
1. **Register**: Create an account with name, phone, email, and password
2. **Login**: Access your account using email and password
3. **Submit Complaint**: 
   - Select complaint category
   - Provide detailed description
   - Add location details (District, Mandal, Ward)
   - Upload supporting photo (optional)
4. **Track Complaints**: View all your complaints and their current status
5. **Password Reset**: Use "Forgot Password" if you need to reset your password

### For Officers
1. **Login**: Use your officer credentials (role must be set to 'Officer')
2. **View Assigned Complaints**: See complaints from your department and assigned location
3. **Update Status**: Change complaint status and add remarks
4. **Monitor Progress**: Track resolution of complaints in your jurisdiction

### For Administrators
1. **Login**: Use admin credentials (is_admin must be True)
2. **Enter Admin Password**: Provide additional admin password (default: 12345678)
3. **View All Complaints**: Access complete system overview
4. **Manage Complaints**: Update any complaint status and add remarks
5. **System Oversight**: Monitor overall system performance

## File Structure
```
vgrs/
├── app.py                      # Main Flask application with routes
├── models.py                   # Database models (User, Complaint)
├── init_db.py                  # Database initialization script
├── seed.py                     # Sample data seeding script
├── requirements.txt            # Python dependencies
├── README.md                   # Project documentation
├── TODO.md                     # Development checklist
├── templates/                  # HTML templates
│   ├── base.html              # Base template with navigation
│   ├── home.html              # Landing page
│   ├── register.html          # User registration
│   ├── login.html             # User login
│   ├── forgot_password.html   # Password reset request
│   ├── reset_password.html    # Password reset form
│   ├── submit_complaint.html  # Complaint submission form
│   ├── track_complaint.html   # Complaint tracking page
│   ├── admin_login.html       # Admin password verification
│   ├── admin_dashboard.html   # Admin complaint management
│   ├── officer_dashboard.html # Officer complaint management
│   └── contact.html           # Contact information
├── static/                     # Static files
│   ├── css/                   # Stylesheets
│   ├── js/                    # JavaScript files
│   └── uploads/               # Uploaded complaint photos
└── instance/
    └── vgrs.db                # SQLite database (created after init)
```

## Database Schema

### Users Table
- `id`: Primary key
- `name`: User's full name
- `phone`: Contact number
- `email`: Unique email address
- `password`: Hashed password
- `is_admin`: Boolean flag for admin access
- `role`: User role (Citizen/Officer)
- `department`: Assigned department (for Officers)
- `assigned_district`: Assigned district (for Officers)
- `assigned_mandal`: Assigned mandal (for Officers)
- `reset_token`: Password reset token
- `reset_token_expiry`: Token expiration timestamp
- `created_at`: Account creation timestamp

### Complaints Table
- `complaint_id`: Primary key
- `user_id`: Foreign key to Users table
- `category`: Complaint category
- `department`: Auto-assigned department
- `description`: Complaint details
- `state`: State (default: Andhra Pradesh)
- `district`: District location
- `mandal`: Mandal location
- `ward`: Ward/village location
- `photo`: Path to uploaded photo
- `status`: Current status (Submitted/In Progress/Resolved/Rejected)
- `officer_remarks`: Officer/Admin comments
- `created_at`: Submission timestamp
- `updated_at`: Last update timestamp

## Security Features
- Password hashing using Werkzeug's security utilities
- Session-based authentication with Flask-Login
- CSRF protection through Flask forms
- Secure file upload handling with filename sanitization
- Role-based access control (RBAC)
- Two-factor admin authentication
- Token-based password reset with expiration

## Default Credentials
**Admin Password**: 12345678 (Change this in production!)

## Future Enhancements
- Email notification system for complaint updates
- SMS alerts for status changes
- Advanced analytics and reporting dashboard
- Complaint priority levels
- Multi-language support
- Mobile application
- Real-time chat support
- Complaint escalation workflow
- Performance metrics and KPIs

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License
This project is licensed under the MIT License.

## Support
For issues, questions, or suggestions, please use the contact page or create an issue in the repository.

---
**Last Updated**: January 2026  
**Version**: 1.0.0
