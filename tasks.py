from storage import task_database, save_data

def add_task(username):
    task = input("Enter task: ")
    if username not in task_database:
        task_database[username] = []
    task_database[username].append(task)
    save_data()
    print("Task added successfully!")

def view_tasks(username):
    print("\n--- Your Tasks ---")
    tasks = task_database.get(username, [])
    if not tasks:
        print("No tasks available.")
    else:
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def delete_task(username):
    view_tasks(username)
    tasks = task_database.get(username, [])
    if not tasks:
        return
    try:
        task_num = int(input("Enter task number to delete: ")) - 1
        if 0 <= task_num < len(tasks):
            task_database[username].pop(task_num)
            save_data()
            print("Task deleted successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input!")


def update_task(username):
    """Updates a selected task."""
    view_tasks(username)
    tasks = task_database.get(username, [])
    if not tasks:
        return
    try:
        task_num = int(input("Enter task number to update: ")) - 1
        if 0 <= task_num < len(tasks):
            new_task = input("Enter new task description: ")
            task_database[username][task_num] = new_task
            save_data()
            print("Task updated successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input!")