import random

answer = random.randint(1, 100)
is_number = True
attempt = 1


while is_number:

    print("Choose a number between 1-100")
    guess = int(input(f"{attempt}. guess: "))
    
    if not (1 <= guess <= 100):
         print("Wrong form")
         continue
    if guess > answer:
        print("Too much")
        attempt += 1
    elif guess < answer:
        print("Too low")
        attempt += 1
    elif answer == guess:
        is_number = False

    

print("Congratulation! You won.")
print(f"You guesses: {attempt}")



