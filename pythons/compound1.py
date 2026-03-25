#Make a compound interest calculator with A = P(1 + r / n)¹

while True:
    principle = float(input("Enter the principle amount: "))
    if principle <= 0:
        print("It's not validated.")
    else:
        break

while True:
    rate = float(input("Enter the rate amount: "))
    if rate <= 0:
        print("It's not validated.")
    else:
        break

while True:
    time = float(input("Enter the time amount: "))
    if time <= 0:
        print("It's not validated.")
    else:
        break       
    
    
print(f"The compound interest will be: {principle * pow(1 + rate / 100, time):.2f}")