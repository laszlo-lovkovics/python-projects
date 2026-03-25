print("Hi")
unit = str(input("Kilograms or Pounds? (K or P): "))
weight = float(input("Please enter your current weight: "))

if unit == "K":
    weight = weight * 2.205
    unit = "Lbs"    
    print (f"Your weight in {unit} is {round(weight, 2)}")
elif unit == "P":
    weight = weight / 2.205
    unit = "Kgs"
    print (f"Your weight in {unit} is {round(weight, 2)}")
else:
    print(f"{unit} isn't correct")

