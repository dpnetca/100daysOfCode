import random
from art import rock, paper, scissors

options = [rock, paper, scissors]
cpu_choice = random.randint(0, 2)

user_choice = int(
    input("What do you choose? 0 for Rock, 1 for Paper or 2 for Scissors\n ")
)

if not (0 < user_choice < 2):
    print("invalid input...you forfeit")
else:
    print(options[user_choice])

    print("Computer chose:")
    print(options[cpu_choice])

    if user_choice == cpu_choice:
        print("It's Draw ")

    elif user_choice == 0 and cpu_choice == 2:
        print("You Win!!")

    elif user_choice == 2 and cpu_choice == 0:
        print("You Lose")

    elif user_choice > cpu_choice:
        print("You Win")

    else:
        print("You Lose")
