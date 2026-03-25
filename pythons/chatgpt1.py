def show_tasks(tasks):
    if not tasks:
        print("There is no tasks")
    else:
        print(f"You have {len(tasks)} tasks")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task(tasks):
    new_task = input("Enter a tasks: ")
    tasks.append(new_task)
            
def remove_task(tasks):
    if not tasks:
        print("No tasks to remove")
    else:    
        print(f"You have {len(tasks)} tasks")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
        try:
            remove = int(input("Enter task number to delete: "))
            if remove < 1 or remove > len(tasks):
                print("Invalid number")
            else:
                confirm = input("Are you sure? (y/n): ")
                if confirm != "y":
                    print("Task has not deleted.")
                else:
                    tasks.pop(remove - 1)
                    print("Task deleted")
        except ValueError:
            print("ONLY NUMBERS")

def tasks_clear(tasks):
    confirm = input("Are you sure? (y/n): ")
    if confirm != "y":
        print("Tasks are not cleared")
    else:
        tasks.clear()

    
def main():
    
    tasks = []
    running = True

    while running:

        print("\nTODO LIST")
        print("1 - Show tasks")
        print("2 - Add task")
        print("3 - Remove task")
        print("4 - Exit")
        print("5 - Clear all tasks")
        print()
        choice = input("Choose option (1-5): ")
        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            break
        elif choice == "5":
            tasks_clear(tasks)
        else:
            print("Invalid form")
            continue

    print("*********")
    print("Good bye")
    print("*********")

if __name__ == '__main__':
    main()