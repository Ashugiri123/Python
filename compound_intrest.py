principle = 0 
rate = 0
time = 0

while principle <= 0:
    principle = float(input("Enter the principle amount : "))
    if principle <= 0:
        print("Principle amount must be greater than 0. Please try again.")
while rate <= 0:
    rate = float(input("Enter the rate of interest (in %): "))
    if rate <= 0:
        print("Rate of interest must be greater than 0. Please try again.")
while time <= 0:
    time = float(input("Enter the time period (in years): "))
    if time <= 0:
        print("Time period must be greater than 0. Please try again.")

amount = principle * pow((1 + rate / 100), time)
compound_interest = amount - principle
print(f"The compound interest after {time} years is: {round(compound_interest, 2)}")
print(f"The total amount after {time} years is: {round(amount, 2)}")
