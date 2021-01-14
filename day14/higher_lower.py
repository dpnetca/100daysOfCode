#!/usr/bin/env python

import random
import os

import game_data

LOGO = "\nHigher or Lower\n"


def clear():
    """issue clear screen command, "clear" for linux/mac "cls" for windows"""
    os.system("cls" if os.name == "nt" else "clear")


def get_valid_input(question, options):
    """Ask user for input, valid, reprompt if invalid

    Args:
        question (str): Question to prompt user
        options (list): list of valid inputs

    Returns:
        valid_input (str): validated input
    """
    while True:
        user_in = input(question)
        if user_in.lower() not in options:
            print(f"{user_in} is not valid input, please try again ")
        else:
            return user_in


def print_option(selection, option):
    """take in the option and print out formatted string

    Args:
        selection (str): Option Label
        option (dict): option to print
    """
    print(
        f"Option {selection}: {option['name']}, "
        f"a {option['description']}, "
        f"from {option['country']}"
    )


def is_correct(guess, options):
    """take in guess and options, compare follower count
    if the guess is the higher follower account return True,
    if not return False

    Args:
        guess (str): guessed option (a or b)
        options (Dict): dictionary of options

    Returns:
        bool: true if guessed correct else false
    """
    if guess.lower() == "a":
        if options["a"]["follower_count"] > options["b"]["follower_count"]:
            return True
    else:
        if options["b"]["follower_count"] > options["a"]["follower_count"]:
            return True
    return False


def play_game():
    print(LOGO)
    options = {"a": random.choice(game_data.data)}
    correct_answer = 0
    correct = True

    while correct:
        options["b"] = random.choice(game_data.data)

        # BUG what happens when a and b are same value...
        # should add some error checking to regenerate b until it is not equal
        # to a

        print_option("A", options["a"])
        print("  -- VS --  ")
        print_option("B", options["b"])
        guess = get_valid_input(
            f"\nWho has the most followers on Instagram "
            f"({', '.join(options.keys()).upper()})? ",
            options.keys(),
        )
        correct = is_correct(guess, options)

        if correct:
            correct_answer += 1
            clear()
            print(LOGO)
            print(f"Correct, your current score is {correct_answer}\n")
            options["a"] = options[guess.lower()]
        else:
            print(
                "Sorry, that is incorrect, your final score is "
                f"{correct_answer}"
            )


clear()
play_game()
