def show_balance():
    print(f"Your balance is: {balance:.2f}")

def deposit():
    amount = float(input("Enter the amount: "))
    if amount < 0:
        print("Invalid form")
        return 0
    else:
        return amount
 
def withdraw():
    amount = float(input("Enter the amount: "))
    if amount < 0 or amount > balance:
        print("Invalid form")
        return 0
    else:
        return amount

def main():
    global balance
    is_running = True

    while is_running:

        print("Banking program")
        space()
        print("1. Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        space()

        choice = input("Select a number (1-4): ")

        match choice:
            case "1":
                show_balance()
            case "2":
                balance += deposit()
            case "3":
                balance -= withdraw()
            case "4":
                is_running = False
            case _:
                print("Invalid number")                  


def space():
    print('***************')
balance = 0


main()
space()
space()
print("Goodbye")
space()
space()

if __name__ == '__main__':
    main()
