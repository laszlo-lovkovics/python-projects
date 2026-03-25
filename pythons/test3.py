import math

print("Hey, we will calcute the hypotenuse of the triangle")
a = float(input("Please enter a: "))
b = float(input("Please enter b: "))

hypotenuse = math.sqrt(pow(a, 2) + pow(b, 2))

print(f"This is your hypotenuse: {round(hypotenuse, 2)}cm")
