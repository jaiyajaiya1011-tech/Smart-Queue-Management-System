# Smart Queue Management System

A web-based Smart Queue Management System developed using Flask, SQLite, HTML, CSS, and JavaScript. The system helps manage digital tokens, monitor waiting customers, and control the service queue through user and admin dashboards.

## Features

- Digital token generation
- Service selection
- Automatic token numbering
- Real-time queue status
- Waiting customer count
- Currently serving token
- Estimated waiting time
- User dashboard
- Admin dashboard
- Call next token functionality
- Token status management
- Waiting, Serving, and Completed status
- User registration and login
- Form validation
- Responsive design for mobile devices
- SQLite database integration

## Technologies Used

- Python
- Flask
- SQLite
- HTML5
- CSS3
- JavaScript

## Project Structure

```text
Smart-Queue-Management-System/
│
├── app.py
├── database.py
├── queue.db
├── README.md
│
├── templates/
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   ├── token.html
│   ├── user_dashboard.html
│   └── admin_dashboard.html
│
└── static/
    ├── style.css
    └── script.js
System Modules

1. Digital Token Generation
Users can select a service and generate a digital token.

2. User Dashboard
The user dashboard displays:
User token
Currently serving token
People waiting
Estimated waiting time
Current queue status

3. Admin Dashboard
The admin dashboard provides:
Total tokens issued
Currently serving token
Waiting customers
Completed tokens
Queue table
Call Next Token functionality

4. Queue Management
The queue follows the status flow:

Waiting → Serving → Completed

When the admin selects Call Next Token, the current serving token is completed and the next waiting token becomes the serving token.

Database

The project uses SQLite for storing:

User details
Token numbers
Service information
Token status

Installation
Step 1: Clone the Repository
git clone https://github.com/yourusername/Smart-Queue-Management-System.git

Step 2: Open the Project
cd Smart-Queue-Management-System

Step 3: Install Flask
pip install flask

Step 4: Run the Application
python app.py

Step 5: Open in Browser
http://127.0.0.1:5000

How It Works

1.User opens the Smart Queue Management System.
2.User selects a required service.
3.A digital token is generated.
4.The token is added to the waiting queue.
5.Admin monitors the queue through the Admin Dashboard.
6.Admin clicks Call Next Token.
7.The next waiting token becomes the serving token.
8.The previous serving token is marked as completed.
.Users can monitor their queue status through the User Dashboard.

Future Enhancements

SMS and email notifications
QR code based token generation
Multiple service counters
Advanced queue analytics
Daily and monthly reports
Online appointment booking
Cloud database integration
Live display screen for token announcements

Project Objective

The main objective of this project is to reduce physical waiting time and improve queue management by providing a digital token-based queue system with separate user and admin dashboards.

Author

Jaiya Dharshini RS

License

This project is developed for educational and academic purposes.