## TO DO LIST (CLI)

tasks = []

def add_task(task):
    tasks.append(task)

def view_tasks():
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

def remove_task(index):
    if 1 <= index <= len(tasks):
        tasks.pop(index - 1)
    else:
        print("Invalid task number.")

def main():
    while True:
        print("\nTO DO LIST")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            task = input("Enter the task: ")
            add_task(task)
            print(f"Task '{task}' added.")
        elif choice == '2':
            print("\nYour Tasks:")
            view_tasks()
        elif choice == '3':
            view_tasks()
            try:
                index = int(input("Enter the task number to remove: "))
                remove_task(index)
                print(f"Task {index} removed.")
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '4':
            print("Exiting the TO DO LIST. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()