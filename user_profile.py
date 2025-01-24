from storage import user_database, save_data
from tasks import add_task, view_tasks, delete_task, update_task

def view_profile(username):
    user = user_database[username]
    print(f"\n--- Profile ---")
    print(f"Name: {user['name']}")
    print(f"Address: {user['address']}")
    print(f"Phone: {user['phone']}")
    print(f"Date of Birth: {user['dob']}")

def change_password(username):
    print("\n--- Change Password ---")
    old_password = input("Enter your current password: ")
    if user_database[username]["password"] != old_password:
        print("Incorrect current password! Password not changed.")
        return
    new_password = input("Enter a new password (min 6 chars): ")
    if len(new_password) < 6:
        print("Password must be at least 6 characters long!")
        return
    user_database[username]["password"] = new_password
    save_data()
    print("Password updated successfully!")

def user_dashboard(username):
    while True:
        print(f"\n--- Dashboard: {username} ---")
        print("1. View Profile")
        print("2. Change Password")
        print("3. Add Task")
        print("4. View Tasks")
        print("5. Delete Task")
        print("6. Update Task")
        print("7. Logout")
        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            view_profile(username)
        elif choice == "2":
            change_password(username)
        elif choice == "3":
            add_task(username)
        elif choice == "4":
            view_tasks(username)
        elif choice == "5":
            delete_task(username)
        elif choice == "6":
            update_task(username)
        elif choice == "7":
            print(f"Goodbye, {username}!")
            break
        else:
            print("Invalid choice! Please try again.")
