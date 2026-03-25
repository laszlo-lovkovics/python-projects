print("Guess the number between 1-100")
print("You have 5 attempts.")

number = 0
attempts = 0
import random
import sys
answer = random.randint(1, 100)


while number != answer:
  number = int(input("Number: "))
  distance = abs(answer - number)
  attempts += 1 
  if attempts == 5:
    print("---------")
    print("GAME OVER")
    sys.exit()
  if number > 100 or number < 1:
    print("Please pay attention for only using 1-100")
    attempts -= 1 
  elif distance > 30:
    print("way too far")
  elif distance > 15:
    print("far")
  elif distance > 5:
    print("close")
  elif 5 >= distance:
    print("very close")
  

print("Nice, you won")
print(f"Attempts: {attempts}")

    