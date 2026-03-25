print("Hey, welcome to my first calculator program!")

operator = input("Please enter your operator. (+, -, *, /): ")
a = float(input("Enter your first number: "))
b = float(input("Enter your second number: "))

if operator == "+":
    print(round(a + b, 3))
elif operator == "-":
    print(round(a - b, 3))
elif operator == "*":
    print(round(a * b, 3))
elif operator == "/":
    print(round(a / b, 3))
else:
    print("Your operator isn't correct!")

