# Password Generator Project
import random
from components import letters, numbers, symbols


print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91
password = []
for _ in range(0, nr_letters):
    password.append(random.choice(letters))

for _ in range(0, nr_symbols):
    password.append(random.choice(symbols))

for _ in range(0, nr_numbers):
    password.append(random.choice(numbers))
# Alternatively - but not in line with course material:
# password.extend(random.choices(letters, k=nr_letters))
# password.extend(random.choices(symbols, k=nr_symbols))
# password.extend(random.choices(numbers, k=nr_numbers))


print("EASY PW:")
print("".join(password))
# Alternatively - more in line with course materiial then join:
# password_string = ""
# for letter in password:
#   password_string += letter


# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
random.shuffle(password)
print("HARD PW:")
print("".join(password))
