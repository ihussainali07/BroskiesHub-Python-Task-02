todo_list = []

def show_menu():
    print("\n==== TO-DO LIST MENU ====")
    print("1. View To-Do List")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Mark Task as Done")
    print("5. Exit")

def view_tasks():
    if not todo_list:
        print("\nYour to-do list is empty.")
    else:
        print("\nYour To-Do List:")
        for idx, task in enumerate(todo_list, 1):
            status = "✔" if task['done'] else "✘"
            print(f"{idx}. [{status}] {task['task']}")

def add_task():
    task = input("Enter the task: ")
    todo_list.append({"task": task, "done": False})
    print("Task added successfully!")

def remove_task():
    view_tasks()
    try:
        task_num = int(input("Enter the task number to remove: "))
        removed = todo_list.pop(task_num - 1)
        print(f"Removed task: {removed['task']}")
    except (IndexError, ValueError):
        print("Invalid task number.")

def mark_done():
    view_tasks()
    try:
        task_num = int(input("Enter the task number to mark as done: "))
        todo_list[task_num - 1]['done'] = True
        print("Task marked as done!")
    except (IndexError, ValueError):
        print("Invalid task number.")

# Main loop
while True:
    show_menu()
    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        view_tasks()
    elif choice == '2':
        add_task()
    elif choice == '3':
        remove_task()
    elif choice == '4':
        mark_done()
    elif choice == '5':
        print("Exiting To-Do List App. Goodbye!")
        break
    else:
        print("Invalid choice. Please select from 1 to 5.")
