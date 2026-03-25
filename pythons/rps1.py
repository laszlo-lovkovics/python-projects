print("Welcome to my rock, paper, scissors game")

import random
elements = ("rock", "paper", "scissors")


while True:


    computer = random.choice(elements)

    choice = input("Choose an element (rock, paper, scissors): ")
   
    if choice not in elements:
        continue
    elif choice == computer:
        print("It's a tie.")
    elif choice == "paper" and computer == "rock":
        print("You won!")
    elif choice == "rock" and computer == "scissors":
        print("You won!")
    elif choice == "scissors" and computer == "paper":
        print("You won!")
    else:
        print("You lost")
    
    if input("Play again? (yes or no): ") != "yes":
       break


         
  
print("Good game")                  