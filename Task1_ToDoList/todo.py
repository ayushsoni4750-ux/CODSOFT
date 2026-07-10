"""
Task 1 - To-Do List Application
CodSoft Python Programming Internship

A simple command-line To-Do List app that lets the user
add, view, update, and delete tasks. Tasks are saved to a
text file so they persist between runs.
"""

import os

FILE_NAME = "tasks.txt"


def load_tasks():
    """Read tasks from the file and return them as a list."""
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as f:
        return [line.strip() for line in f.readlines() if line.strip()]


def save_tasks(tasks):
    """Write the current list of tasks back to the file."""
    with open(FILE_NAME, "w") as f:
        for task in tasks:
            f.write(task + "\n")


def view_tasks(tasks):
    print("\n--- YOUR TO-DO LIST ---")
    if not tasks:
        print("No tasks yet. Add one!")
    else:
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
    print("-----------------------\n")


def add_task(tasks):
    task = input("Enter new task: ").strip()
    if task:
        tasks.append(task)
        save_tasks(tasks)
        print("Task added successfully!\n")
    else:
        print("Task cannot be empty.\n")


def update_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        num = int(input("Enter task number to update: "))
        if 1 <= num <= len(tasks):
            new_task = input("Enter new task text: ").strip()
            if new_task:
                tasks[num - 1] = new_task
                save_tasks(tasks)
                print("Task updated successfully!\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Please enter a valid number.\n")


def delete_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        num = int(input("Enter task number to delete: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            save_tasks(tasks)
            print(f"Deleted: {removed}\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Please enter a valid number.\n")


def main():
    tasks = load_tasks()
    while True:
        print("===== TO-DO LIST MENU =====")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            update_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Goodbye! Keep crushing your tasks.")
            break
        else:
            print("Invalid choice. Please select between 1-5.\n")


if __name__ == "__main__":
    main()
