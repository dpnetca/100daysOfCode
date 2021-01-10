# /usr/env/python
"""
BLACKJACK Project
Day 11 Capstone Project
https://www.udemy.com/course/100-days-of-code
written by Denis Pointer

Our Blackjack House Rules
- The deck is unlimited in size.
- There are no jokers.
- The Jack/Queen/King all count as 10.
- The the Ace can count as 11 or 1.
- Use the following list as the deck of cards:
- cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
- The cards in the list have equal probability of being drawn.
- Cards are not removed from the deck as they are drawn.
- The computer is the dealer.
"""
import random
import os

import art


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
        if user_in not in options:
            print(f"{user_in} is not valid input, please try again ")
        else:
            return user_in


def deal_card(deck, hand):
    """Simply choose a random card and assign to hand. no return, instead
    rely's on mutability of passed in list, maybe not a good practice
    created as a function for now to allow for future possible error checking
    and functionality (such as poppying card out of deck instead of
    infinite deck)


    Args:
        deck (list): list of integers representing cards in deck
        hand (list): list of integers representing cards in hand
    """
    hand.append(random.choice(deck))


def deal_hands(deck, players_list, cards_to_deal=2):
    """cycle through players deal one card to each player until identified
    number of cards is dealt

    Args:
        deck (List of Int): List of integers representing card values
        players_list (List of Str): List of player names
        cards_to_deal (int, optional): number of cards to deal to each player
            Defaults to 2.

    Returns:
        players (Dict): dictionary where
            key = player name,
            value= list of cards
    """
    players = {}

    for card_index in range(cards_to_deal):
        for player in players_list:
            # get the players hand, if no hand exists, create an empty hand
            hand = players.get(player, [])
            deal_card(deck, hand)
            players[player] = hand
    return players


def sum_hand(hand):
    """sum up hand value.  If the hand value > 21, and the hand contains an
    ace (11) change the ace to a value of 1 and repeat until hand value is
    less than 21, or no more aces are present
    rely's on mutability of passed in list, to update the had maybe not a
    good practice

    Args:
        hand (list): list of integers representing cards in hand

    Returns:
        int: value of hand
    """
    while True:
        hand_value = sum(hand)
        if hand_value > 21 and 11 in hand:
            index_11 = hand.index(11)
            hand[index_11] = 1
        else:
            return hand_value


def play_game(name, player_stats):
    # initate game variables
    game_over = False
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    # define players in a list to allow for future of more then 1 human
    # for now players[0] = humand and players[1] = computer
    players = [name, "Computer"]
    hand_values = {}

    # Deal initial hands
    hands = deal_hands(deck=cards, players_list=players)

    # get sum of initial hands for all players
    for player in players:
        hand_values[player] = sum_hand(hands[player])

    # check for blackjack
    if 21 in hand_values.values():
        game_over = True
        print(art.logo)
        print(f"Computer hand: {hands[players[1]]}")
        print(f"Your hand: {hands[players[0]]}")
        if hand_values[players[0]] == hand_values[players[1]]:
            print("DOUBLE BLACKJACK")
            player_stats["draws"] += 1
        elif hand_values[players[0]] == 21:
            print(f"BLACKJACK for {players[0]}")
            player_stats["wins"] += 1
        else:
            print(f"BLACKJACK for {players[1]}")
            player_stats["losses"] += 1

    # loop until the game is done
    while not game_over:
        # display current hands
        print(art.logo)
        print(f"Computer visible card: {hands[players[1]][1]}")
        print(f"Your hand: {hands[players[0]]}")

        # get user choice
        move = get_valid_input(
            "Would you like to (h)it or (s)tay (h or s)? ", ["h", "s"]
        )
        if move == "h":
            # deal card and display
            deal_card(deck=cards, hand=hands[players[0]])

            # get hand value, if > 21 end game
            hand_values[players[0]] = sum_hand(hands[players[0]])
            if hand_values[players[0]] > 21:
                player_stats["losses"] += 1
                game_over = True
                print(f"You are dealt a {hands[players[0]][-1]} ")
                print("BUSTED")
                print(f"{hands[players[0]]} = {hand_values[players[0]]}")
                print(f"sorry {players[0]}, you lose")

            else:
                clear()
        else:
            game_over = True
            clear()
            print(art.logo)

            # if human stayed (only other option) play computer hand
            # computer hits on 16 and under, stays on 17 or over
            while hand_values[players[1]] < 17:
                deal_card(deck=cards, hand=hands[players[1]])
                hand_values[players[1]] = sum_hand(hands[players[1]])

            # display final hands and values
            print("Final Hands:")
            for p in players:
                print(f"{p}: {hands[p]} Total: {hand_values[p]}")

            # see who won and display
            if hand_values[players[1]] > 21:
                print(f"{players[1]} Busted")
                print(f"Congratulations {players[0]} you win!")
                player_stats["wins"] += 1
            elif hand_values[players[1]] > hand_values[players[0]]:
                print(f"Sorry {players[0]}, {players[1]} wins")
                player_stats["losses"] += 1
            elif hand_values[players[1]] == hand_values[players[0]]:
                print("Draw")
                player_stats["draws"] += 1
            else:
                print(f"Congratulations {players[0]} you win!")
                player_stats["wins"] += 1

    # play_again?
    if get_valid_input("Play again (y or n)? ", ["y", "n"]) == "y":
        clear()
        play_game(name, player_stats)
    else:
        print("Thank you for playing")
        print(f"Final Stats for {players[0]}: ")
        for k, v in player_stats.items():
            print(f"    {k}: {v}")


def prompt_for_game():
    clear()
    play = get_valid_input(
        "Do you want to play a game of Blackjack? (y or n)? ", ["y", "n"]
    )

    if play == "y":
        name = input("What is your name? ")
        clear()
        player_stats = {
            "wins": 0,
            "losses": 0,
            "draws": 0,
        }
        play_game(name, player_stats)
    else:
        return


if __name__ == "__main__":
    prompt_for_game()
