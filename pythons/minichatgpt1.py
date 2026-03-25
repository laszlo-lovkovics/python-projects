import random

words = ["apple", "pineapple", "pearl"]
word = random.choice(words)
displays = ["_"] * len(word)
attempts = 0
used= []
print(" ".join(displays))
while True:

    guess = input("Guess the letter: " ).lower()
    if len(guess) != 1:
        print("You can only choose 1 letter once.")
        continue

    
    if guess in used:
        print("You had guessed this letter")
        continue
    
    used.append(guess)
    print(f"Used letters: {', '.join(used)}")
    if guess not in word:
        attempts += 1
        if attempts >= 10:
            print("You lost")
            break

        print("Wrong")
        print(f"You have {10 - attempts} left")
        continue

    
    for index, letter in enumerate(word):
        if letter == guess:
            displays[index] = guess

    print(" ".join(displays))

    if "_" not in displays:
        print("You won")
        break

