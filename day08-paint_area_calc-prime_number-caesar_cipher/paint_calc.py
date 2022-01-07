# Write your code below this line 👇


def paint_calc(height, width, cover):
    cans = height * width / cover
    cans_needed = round(cans + 0.5)
    # could do something with // % and if statements
    # could use math.ceil

    print(f"You'll need {cans_needed} cans of paint.")


# Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
