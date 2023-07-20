##To do list: Develop a program that allows the user to manage their tasks by adding,removing, and displaying them.

tasks = [1, 23, 54, 78, 987]

def add_task():
    task = int(input("Enter the task to add: "))
    tasks.append(task)
    print("Task added successfully!")
def remove_task():
    if not tasks:
        print("No tasks to remove.")
        return
    print("Current tasks:")
    
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

    try:
        index = int(input("Enter the task number to remove: ")) - 1
        if 0 <= index < len(tasks):
            removed_task = tasks.pop(index)
            print(f"Removed: {removed_task}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def display_tasks():
    if not tasks:
        print("No tasks added yet.")
        return
    print("Tasks:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")
def main():
    while True:
        print("\n===== To-Do List Manager =====")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Display Tasks")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            add_task()
        elif choice == '2':
            remove_task()
        elif choice == '3':
            display_tasks()
        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()



    



































