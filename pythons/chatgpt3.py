import random


def main():

    print("******************")
    print("Hey, it's a guess number game.")
    print("******************")

    attempts = 0
    is_running = True

    while is_running:
        
        print("1 - Easy (1-50)")
        print("2 - Medium (1-100)")
        print("3 - Hard (1-500)")

        difficulty = input("Choose the difficulty (1/2/3): ")
        if difficulty in ("1", "2", "3"):
            print("")
        else:
            print("Wrong form")
            continue

        match difficulty:
            case "1":
                print("Easy mode has started")
                min_num = 1
                max_num = 50
            case "2":
                print("Medium mode has started")
                min_num = 1
                max_num = 100
            case "3":
                print("Hard mode has started")
                min_num = 1
                max_num = 500

        generated = random.randint(min_num, max_num)
        
        while True:
            try:
                guess = int(input(f"Guess the number between {min_num} and {max_num}: "))
                if guess < min_num or guess > max_num:
                    print("Invalid number")
                    continue
            except ValueError:
                print("Wrong form")
                continue
            
            attempts += 1
            
            if guess == generated:
                print("You won")
                break
            elif guess > generated:
                print("Too high")
            elif guess < generated:
                print("Too low")


        print(f"You attempts: {attempts}")

        again = input("Play again? (y/n): ")
        if again == "y":
            attempts = 0
            continue
        else:
            break




    print("Goodbye")
    
        
        

if __name__ == '__main__':
    main()