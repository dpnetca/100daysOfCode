# If the bill was $150.00, split between 5 people, with 12% tip.
# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60


print("Welcome to the top calculator")
bill = input("What was the total bill? $")
tip = input("What percentage tip would you like to give? 10, 12, or 15? ")
split = input("How many people to split the bill? ")

total = float(bill) * float("1." + tip)
share = total / float(split)

print(f"Each person should pay: ${round(share,2):.2f}")
