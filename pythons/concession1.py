menu = {"pizza" : 4.79, 
        "hamburger" : 3.29, 
        "small fries" : 2.89, 
        "large fries" : 3.89}

total = 0
cart = []

print("------Menu------")
for key, value in menu.items(): 
    print(f"{key}  {value}")
print("----------------")

while True:
    food = input("Enter the food to buy, only (q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        print(f"{food} added to your cart")
        cart.append(food)
    else:
        print("Its not on the list!")


for food in set(cart):
    amount = cart.count(food)
    print(amount,  food)
    total += menu.get(food) * amount



print(f"Your cart costs: {total}")





