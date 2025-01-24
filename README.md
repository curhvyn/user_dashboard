# User Authentication & Task Management System

## Overview
This project is a **User Authentication and Task Management System** built in Python. It allows users to:
- Register with a username, password, and additional details.
- Log in securely.
- View and update their profile information.
- Manage tasks (add, view, delete, update tasks).
- Persist user and task data using JSON storage.

## Features
### **User Authentication**
- Register users with a **username**, **password**, **full name**, **address**, **phone number**, and **date of birth**.
- Enforce password validation (minimum 6 characters).
- Validate phone numbers (10-digit format).
- Validate date of birth (must be in `YYYY-MM-DD` format and cannot be a future date).
- Secure user login with stored credentials.

### **Task Management**
- Add tasks after logging in.
- View a list of tasks.
- Delete tasks by selecting the task number.
- Update tasks by modifying existing entries.

## Installation
### **Prerequisites**
Ensure you have **Python 3.x** installed. You can check your version with:
```sh
python --version
```

### **Cloning the Repository**
```sh
git clone https://github.com/curhvyn/user_dashboard.git
cd user_dashboard
```

## Running the Application
Execute the script with:
```sh
python main.py
```

## Project Structure
```
project/
│── main.py               # Main entry point of the program
│── auth.py               # Handles user registration & authentication
│── user_profile.py       # Handles user dashboard and profile management
│── tasks.py              # Manages task creation, deletion, and updates
│── storage.py            # Handles data persistence (saving/loading JSON files)
│── users.json            # User data storage
│── tasks.json            # Task data storage
│── README.md             # Project documentation
```

## Usage Guide
1. **Register a new user**: Enter a username, password, and required profile details.
2. **Log in**: Enter your registered credentials.
3. **Manage profile**: View or update your profile details.
4. **Manage tasks**: Add, view, delete, or update tasks.
5. **Exit**: Quit the application anytime.

## Validations Implemented
- **Phone Number**: Must be exactly **10 digits**.
- **Date of Birth**: Must follow **YYYY-MM-DD format** and **cannot be a future date**.
- **Passwords**: Must be at least **6 characters long**.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes.