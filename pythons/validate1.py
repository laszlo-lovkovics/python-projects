print("Hey, it's an username validator")
user = str(input("What's your username?: "))

if len(user) > 12:
    print("It's too much character")
elif not user.find(' ') == -1:
    print("It must not contain spaces.")
elif not user.isalpha():
    print("It must contain only alphas")
else:
    print(f"Hey {user.capitalize()}, your username is valid")
    