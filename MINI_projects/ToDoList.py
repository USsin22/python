
import os
import json

TODO_FILE = "todo_data.json"

def load_todos():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as f:
            return json.load(f)
    return []

def save_todos(todos):
    with open(TODO_FILE, "w") as f:
        json.dump(todos, f, indent=2)

def list_todos(todos):
    if not todos:
        print("No tasks in your ToDo list.")
        return
    print("\nYour ToDo List:")
    for idx, todo in enumerate(todos, 1):
        status = "[x]" if todo["done"] else "[ ]"
        print(f"{idx}. {status} {todo['task']}")

def add_todo(todos):
    task = input("Enter a new task: ").strip()
    if task:
        todos.append({"task": task, "done": False})
        save_todos(todos)
        print("Task added!")
    else:
        print("Task cannot be empty.")

def complete_todo(todos):
    list_todos(todos)
    try:
        idx = int(input("Enter the number of the task to mark as complete: "))
        if 1 <= idx <= len(todos):
            todos[idx-1]["done"] = True
            save_todos(todos)
            print("Task marked as complete!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_todo(todos):
    list_todos(todos)
    try:
        idx = int(input("Enter the number of the task to delete: "))
        if 1 <= idx <= len(todos):
            removed = todos.pop(idx-1)
            save_todos(todos)
            print(f"Deleted: {removed['task']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    todos = load_todos()
    while True:
        print("\n--- ToDo List Menu ---")
        print("1. List tasks")
        print("2. Add task")
        print("3. Complete task")
        print("4. Delete task")
        print("5. Exit")
        choice = input("Choose an option (1-5): ").strip()
        if choice == "1":
            list_todos(todos)
        elif choice == "2":
            add_todo(todos)
        elif choice == "3":
            complete_todo(todos)
        elif choice == "4":
            delete_todo(todos)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1-5.")

if __name__ == "__main__":
    main()
