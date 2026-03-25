questions = ("1. What is the capital of France?",
            "2. Which planet is known as the Red Planet?",
            "3. What is 7 × 8?",
            "4. Which language is mainly used for web page styling?",
            "5. Which animal is known as the king of the jungle?")

options = (("A. Berlin", "B. Madrid", "C. Paris", "D. Rome"), 
          ("A. Venus", "B. Mars", "C. Jupiter", "D. Saturn",),
          ("A 54", "B 56", "C 64", "D 58"),
          ("A. HTML", "B. Python", "C. CSS", "D. C++"),
          ("A. Tiger", "B. Lion", "C. Elephant", "D. Gorilla"))

guesses = []
question_num = 0
score = 0

answers = ("C", "B", "B", "C", "B") 

for question in questions:
    print("---------")
    print(question)
    for option in options[question_num]:
        print(option)      

    guess = input("Enter your guess (A B C D): ").upper()
    guesses.append(guess)    
    if guess == answers[question_num]:
        score += 1
        print("CORRECT")
    else:
        print("INCORRECT")
    question_num += 1      

print("--------------")
print("    RESULTS   ")    
print("--------------")

print("Answers: ", end="")
for answer in answers:
    print(answer, end=" ") 
print()

print("Your guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)   
print(f"{score}%")