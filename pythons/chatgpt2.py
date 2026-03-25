import random
import string

def ask_numbers(password):
    numbers = input("Include numbers? (y/n): ")
    if numbers != "y":
        print("No numbers added")
        return password
    else:
        password += string.digits
        print("Numbers added")
        return password
def ask_symbols(password):
    symbols = input("Include symbols? (y/n): ")
    if symbols != "y":
        print("No symbols added")
        return password
    else:
        password += string.punctuation
        print("Symbols added")
        return password





def main():

    password = string.ascii_letters

    while True:
        try:
            length = int(input("Enter password lenght (1-12): "))
            if length > 12 or length < 1:
                print("Invalid number")
                continue
        except ValueError:
            print("Only digits!")
            continue
        else:
            password = ask_numbers(password)
            password = ask_symbols(password)
            break

    real_password = ""
    for _ in range(length):
        real_password += random.choice(password)
    
    print(f"Your random password is: {real_password}")
    
if __name__ == '__main__':
    main()

