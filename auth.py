import json
from storage import save_data, user_database
from user_profile import user_dashboard
from datetime import datetime
import re

def is_valid_phone(phone):
    """Checks if the phone number is a valid 10-digit number."""
    return re.fullmatch(r"\d{10}$", phone) is not None

def is_valid_dob(dob):
    """Checks if the date of birth is valid: format YYYY-MM-DD, valid month/day, and not a future date."""
    try:
        dob_date = datetime.strptime(dob, "%Y-%m-%d")
        if dob_date > datetime.today():
            return False
        return True
    except ValueError:
        return False

def register_user():
    print("\n--- Register ---")
    username = input("Enter a username: ")
    if username in user_database:
        print("Username already exists! Try again.")
        return

    password = input("Enter a password (min 6 chars): ")
    if len(password) < 6:
        print("Password must be at least 6 characters long!")
        return

# Additional user details
    name = input("Enter your full name: ")
    while True:
        address = input("Enter your address: ")
        phone = input("Enter your phone number (10 digits): ")
        if not is_valid_phone(phone):
            print("Invalid phone number! Please enter a 10-digit number.")
            continue
        dob = input("Enter your Date of Birth (YYYY-MM-DD): ")
        if not is_valid_dob(dob):
            print("Invalid DOB format or future date! Please enter a valid past date in YYYY-MM-DD format.")
            continue
        break
    
    user_database[username] = {
        "password": password,
        "name": name,
        "address": address,
        "phone": phone,
        "dob": dob
    }
    save_data()
    print("Registration successful!")

def login_user():
    print("\n--- Login ---")
    username = input("Enter your username: ")
    if username not in user_database:
        print("Username not found! Please register first.")
        return

    password = input("Enter your password: ")
    if user_database[username]["password"] == password:
        print(f"\nWelcome back, {username}!")
        user_dashboard(username)
    else:
        print("Incorrect password! Try again.")
