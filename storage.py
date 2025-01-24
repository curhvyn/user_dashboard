import json

user_database = {}
task_database = {}

def load_data():
    global user_database, task_database
    try:
        with open("users.json", "r") as f:
            user_database = json.load(f)
    except FileNotFoundError:
        user_database = {}

    try:
        with open("tasks.json", "r") as f:
            task_database = json.load(f)
    except FileNotFoundError:
        task_database = {}

def save_data():
    with open("users.json", "w") as f:
        json.dump(user_database, f, indent=4)
    with open("tasks.json", "w") as f:
        json.dump(task_database, f, indent=4)


