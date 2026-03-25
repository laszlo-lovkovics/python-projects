with open("passwords.txt", "a"):
        pass

def add_password():
    service = input("Service: ")
    username = input("Username: ")
    password = input("Password: ")[::-1]
    exist = False
    with open("passwords.txt") as f:
        for line in f:
            parts = line.strip().split(" | ")
            if parts[0] == service and parts[1] == username:
                exist = True
    if not exist:
        with open("passwords.txt", "a") as f:
            f.write(f"{service} | {username} | {password}\n")
            print("*********")
            print("The new datas has added")
            print("*********")
    elif exist:
        print("!!!!!!!!!")
        print("Service and Username are already used")
        print("!!!!!!!!!")


def view_passwords():
    found = False
    with open("passwords.txt") as f:
        for line in f:
            parts = line.strip().split(" | ")
            if len(parts) == 3:
                password = parts[2][::-1]
                print(f"{parts[0]} | {parts[1]} | {password}")
                found = True
    if not found:
        print("*********")
        print("There aren't any passwords") 
        print("*********")

def search_password():
    service = input("What's your service: ")
    found = False
    with open("passwords.txt") as f:
        for line in f:
            parts = line.strip().split(" | ")
            if len(parts) == 3 and service == parts[0]:
                print("Found:")
                password = parts[2][::-1]
                print(f"{parts[0]} | {parts[1]} | {password}")  
                found = True
    if not found:
        print("*********")
        print("Not found") 
        print("*********")

def remove_password():
    found = False
    with open ("passwords.txt") as f:
        for line in f:
            parts = line.strip().split(" | ")
            if len(parts) == 3:
                found = True
    if found:    
        with open("passwords.txt") as f:
            for i, line in enumerate(f):
                parts = line.strip().split(" | ")
                if len(parts) == 3:
                    password = parts[2][::-1]
                    print(f" {i + 1}. {parts[0]} | {parts[1]} | {password}")
        try:
            choice = int(input("Choose to delete (Only digits): "))
            if 1 <= choice:
                with open("passwords.txt") as f:    
                    lines = list(f)
                    parts = lines[choice - 1].strip().split(" | ")
                    password = parts[2][::-1]
                    print(f"{parts[0]} | {parts[1]} | {password} is deleted")
                    del lines[choice - 1]
                with open("passwords.txt", "w") as f:
                    f.writelines(lines)
            else:
                print("*********")
                print("Not found")
                print("*********")
        except (IndexError, ValueError):
            print("*********")
            print("Not found") 
            print("*********")
    elif not found:
        print("*********")
        print("There aren't any passwords to remove") 
        print("*********")

def edit_password():
    found = False
    with open ("passwords.txt") as f:
        for line in f:
            parts = line.strip().split(" | ")
            if len(parts) == 3:
                found = True
    if found:            
        with open("passwords.txt") as f:
            for i, line in enumerate(f):
                parts = line.strip().split(" | ")
                if len(parts) == 3:
                    password = parts[2][::-1]
                    print(f" {i + 1}. {parts[0]} | {parts[1]} | {password}")
        try:
            choose = int(input("Choose a number to change: "))
            with open("passwords.txt") as f:
                lines = list(f)
                parts = lines[choose - 1].strip().split(" | ")
                new_password = input("Write a new password: ")
                parts[2] = new_password[::-1]
                lines[choose - 1] = f"{parts[0]} | {parts[1]} | {parts[2]}\n"
                print("*********")
                print("Updated successfully")
                print("*********")
            with open("passwords.txt", "w") as f:
                f.writelines(lines)
        except (IndexError, ValueError):
                print("*********")
                print("Not found") 
                print("*********")
    elif not found:
        print("*********")
        print("There aren't any passwords to edit") 
        print("*********")
    
    
    
        
def main():
    print("Password manager")
    print("************")

    while True:
        print("1. Add password\n2. View passwords\n3. Search password\n4. Remove task\n5. Edit password\n6. Exit")
        try:
            choice = int(input("Choose between 1 and 6: "))
            if choice == 1:
                add_password()
            elif choice == 2:
                view_passwords()
            elif choice == 3:
                search_password()
            elif choice == 4:
                remove_password()
            elif choice == 5:
                edit_password()
            elif choice == 6: 
                break
            else:
                print("!!!(1 - 6)!!!")
        except ValueError:
            print("!!! Incorrect Form !!!\n")
            continue
    
    
    print("All datas are saved")

if __name__ == '__main__':
    main()