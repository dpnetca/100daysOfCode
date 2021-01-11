#!/usr/bin/env python

import random


def get_str_input(question, valid_input):
    user_in = input(question)
    if user_in in valid_input:
        return user_in
    else:
        print("invalid input, pleae try again")
        return get_str_input(question, valid_input)


def get_int_input(question):
    try:
        user_in = int(input(question))
        return user_in
    except ValueError:
        print("please enter a valid nuber")
        return get_int_input(question)


low = 1
high = 100
number_of_guesses = {"easy": 10, "medium": 7, "hard": 5}


print("Welcome to the Number Guessing Game")

number = random.randint(low, high)
print(f"I am thinking of a number between {low} and {high}")
difficulty = get_str_input(
    f"Choose a difficulty ({', '.join(number_of_guesses.keys())}): ",
    number_of_guesses.keys(),
)

guesses = number_of_guesses[difficulty]
game_on = True

while game_on:
    print(f"You have {guesses} attempts remaining to guess the number")
    guess = get_int_input("Make a guess: ")
    if guess == number:
        print(f"You got it!! the answer was {number}")
        game_on = False
    elif guess > number:
        print("Too high")
    else:
        print("Too low")

    if guesses == 1:
        print("sorry you have run our of guesses, better luck next time")
        game_on = False
    else:
        print("guess again.")
        guesses -= 1
