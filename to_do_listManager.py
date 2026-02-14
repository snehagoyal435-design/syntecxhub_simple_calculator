import json
import os

# Function to save tasks to a JSON file
def save_tasks(tasks):
    with open("todo_list.json", "w") as file:
        json.dump(tasks, file, indent=4)

# Function to load tasks from the file
def load_tasks():
    if not os.path.exists("todo_list.json"):
        return []
    try:
        with open("todo_list.json", "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def main():
    tasks = load_tasks()
    
    while True:
        print("\n--- To-Do List Manager ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Select an option (1-5): ")

        if choice == '1':
            print("\nYOUR TASKS:")
            if not tasks:
                print("Your list is empty.")
            for index, item in enumerate(tasks, 1):
                status = "✔" if item["done"] else " "
                print(f"{index}. [{status}] {item['task']}")

        elif choice == '2':
            new_task = input("Enter the task description: ")
            tasks.append({"task": new_task, "done": False})
            save_tasks(tasks)
            print("Task added successfully!")

        elif choice == '3':
            try:
                task_num = int(input("Enter task number to mark as done: "))
                tasks[task_num - 1]["done"] = True
                save_tasks(tasks)
                print("Task updated!")
            except (ValueError, IndexError):
                print("Invalid task number.")

        elif choice == '4':
            try:
                task_num = int(input("Enter task number to delete: "))
                tasks.pop(task_num - 1)
                save_tasks(tasks)
                print("Task deleted!")
            except (ValueError, IndexError):
                print("Invalid task number.")

        elif choice == '5':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()