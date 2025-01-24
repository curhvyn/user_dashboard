from auth import register_user, login_user
from storage import load_data

# Load stored data
load_data()

# Main loop
while True:
    print("\n--- User Authentication & Task Manager ---")
    print("1. Register")
    print("2. Login")
    print("3. Exit")
    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        register_user()
    elif choice == "2":
        login_user()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice! Please try again.")
