def add_note():
    add = input("Add a note: ")
    with open("notes.txt", "a") as f:
        f.write(f"{add}\n")
        print(f"{add} added to the list")
def view_notes():
    found = False
    with open("notes.txt") as f:
        for x in f:
            if len(x) > 1:
                found = True   
    with open("notes.txt") as f:    
        if found:
            print()
            for i, lines in enumerate(f):
                print(f"{i + 1}. {lines}".strip())
            print("**********")
        elif not found:
            print()
            print("The notes are empty!")  
            print("**********")     
def search_note():
    found = False
    with open("notes.txt") as f:
        for x in f:
            if len(x) > 1:
                found = True
    if found:
        found_inside = False
        search = input("Show a snippet of your notes: ")
        with open("notes.txt") as f:
            for lines in f:
                if search in lines:
                    print(f"{lines.strip()}")
                    found_inside = True

        if not found_inside:
            print("!!!!!!!!!!!!")
            print("No results for your search")
            print("!!!!!!!!!!!!")
    elif not found:
        print()
        print("The notes are empty!")  
        print("**********")  

def delete_note():
    found = False
    with open("notes.txt") as f:
        for x in f:
            if len(x) > 1:
                found = True
    if found:
        with open("notes.txt") as f:
            for i, lines in enumerate(f):
                print(f"{i + 1}. {lines}".strip())
            print("**********")
        try:
            delete = int(input("Choose a number to delete: "))   
            with open("notes.txt") as f:
                if delete > 0:    
                    list_lines = list(f)
                    print(f"{list_lines[delete - 1].strip()} deleted")
                    del list_lines[delete - 1]
                else:
                    raise ValueError    
            with open("notes.txt", "w") as f:
                f.writelines(list_lines)
        except (IndexError, ValueError):
            print("!!!!!!!!!!!!")
            print("Invalid form")
            print("!!!!!!!!!!!!")
    elif not found:
            print()
            print("The notes are empty!")  
            print("**********")

def main():
    with open("notes.txt", "a") as f:
        pass

    print("*************")
    print("CLI Notes app")
    print("*************")
    while True:
        
        print("1. Add note\n2. View notes\n3. Search Note\n4. Delete Note\n5. Exit")
        choose = input("Choose between 1-5: ")
        if choose == "1":
            add_note()
        elif choose == "2":
            view_notes()
        elif choose == "3":
            search_note()
        elif choose == "4":
            delete_note()
        elif choose == "5":
            break
        else:
            print("!!!!!!!!!!!!")
            print("Invalid form")
            print("!!!!!!!!!!!!")

if __name__ == '__main__':
    main()        





