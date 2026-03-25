foods = []
prices = []
total = 0

while True:
    food = str(input("Enter a food to buy (q to quit): "))
    if food == "q":
        break
    else:
        price = float(input("Enter the prize of food: $"))
        foods.append(food)
        prices.append(price)

for food in foods:
    print(food, end=" ")
    print()
    
for price in prices:
    total+= price

print(f"The price will be: ${total:.2f}")


               