import json
import os
from datetime import datetime

FILE_NAME = "tasks.json"

def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except:
        return []

# Save tasks to file

def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)

# Adding task

def add_task(tasks):
    name = input("Enter task: ")
    task = {
        "name": name,
        "status": "Not Completed",
        "created": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    tasks.append(task)
    save_tasks(tasks)
    print("Task added!")

# View tasks

def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return
    print("\n--- TO-DO LIST ---")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task['name']} | {task['status']} | {task['created']}")

# Mark task as completed

def mark_done(tasks):
    view_tasks(tasks)
    try:
        num = int(input("Enter task number to mark as done: "))
        if 1 <= num <= len(tasks):
            tasks[num - 1]["status"] = "Completed"
            save_tasks(tasks)
            print("Task marked as completed!")
        else:
            print("Invalid task number")
    except:
        print("Please enter a valid number")

# Delete task

def delete_task(tasks):
    view_tasks(tasks)
    try:
        num = int(input("Enter task number to delete: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            save_tasks(tasks)
            print(f"Deleted: {removed['name']}")
        else:
            print("Invalid task number")
    except:
        print("Please enter a valid number")

# Main Menu

def main():
    tasks = load_tasks()

    while True:
        print("\n===== TO-DO MENU =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark as Done")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Wow your choice is done...")
            break
        else:
            print("Choose wisely please.Try again.")
if __name__ == "__main__":
    main()