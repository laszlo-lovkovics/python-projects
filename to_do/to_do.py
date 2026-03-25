import os

with open("list.txt", "a"):
        pass

def show_list():
    with open("list.txt") as f:
        print("***************")
        print("Your list has:")
        for i, line in enumerate(f):
            line = line.strip()
            print(f"{i + 1}. {line}")
        print("***************")

def add_task():
    with open("list.txt", "a") as f:
        add_choice = input("Add a task: ")
        f.write(f"{add_choice}\n")
    show_list()


def remove_task():
    show_list()
    try:
        remove_choice = int(input("Choose a task to delete: "))
        f = open("list.txt")
        lines = list(f)
        print(f"{lines[remove_choice - 1].strip()} has been deleted")
        del lines[remove_choice - 1]
        f.close()
        with open("list.txt", "w") as f:
            f.writelines(lines)
    except (IndexError, ValueError):
        print("Wrong format")
    

def clear_all():
    with open("list.txt", "w"):
        pass
    print("***********")
    print("All of the tasks have been deleted")
    print("***********")
    
    
    
def main():

    print("To do list program\n")
    show_list()
    while True:
        print("1. Show tasks\n2. Add task\n3. Remove task\n4. Exit\n5. Delete all tasks")
        choice = input("Choose between (1-5): ")
        if choice == "1":
            show_list()
        elif choice == "2":
            add_task()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            break
        elif choice == "5":
            clear_all()
        else:
            print("!!!!!!!!")
            print("Only (1-5)")
            print("!!!!!!!!")
    
    print("***********")



if __name__ == '__main__':
    main()