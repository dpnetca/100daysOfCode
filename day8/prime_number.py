# Write your code below this line 👇


def prime_checker(number):
    if number < 0:
        print("don't input negative numbers...")
    elif number < 3:
        prime = True
    else:
        prime = True
        for n in range(2, number):
            if number % n == 0:
                prime = False
                break
    if prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")


# Write your code above this line 👆

# Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
