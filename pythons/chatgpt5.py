import random

def chooses():
    words = ["python", "apple", "pineapple", "flower", "javascript"]
    word = random.choice(words)
    return word

def main():
    
    print("It's a Hangman game")
    print("Guess the word")
    print("You have 10 attempt")
    
    word = chooses()

    while True:
        for _ in word:
            print("_", end= " ")
        
        display = ["_"] * len(word)

        choose = input("Choose a letter: ")
        if choose in word:
            display[i] = choose
            
        print(display)  




if __name__ == '__main__':
    main()

