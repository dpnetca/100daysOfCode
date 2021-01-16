#!/usr/bin/env python

from menu import MENU

COIN_VALUES = {
    "quarters": 0.25,
    "dimes": 0.10,
    "nickels": 0.05,
    "pennies": 0.01,
}


def calculate_change(total_money, drink):
    """calcualte change

    Args:
        total_money (float): user input money
        drink (str): user selected drink

    Returns:
        float: change remaining after paying for drink
    """
    return total_money - MENU[drink]["cost"]


def get_coins():
    """for each coin type defined in COIN_VALUES get prompt user for number of
    coins and return a dictionary with the quantity of each coin

    Returns:
        dict: dictionary of coins entered
    """
    coins = {}
    print("Please insert coins")
    for coin in COIN_VALUES:
        coins[coin] = get_int_input(f"How many {coin}?:  ")
    return coins


def get_int_input(question):
    """Ask user for input, verify input is an int

    Args:
        question (str): question to prompt user

    Returns:
        int: user input as int
    """
    try:
        user_in = int(input(question))
        return user_in
    except ValueError:
        print("please enter a valid nuber")
        return get_int_input(question)


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


def make_drink(drink, inventory):
    """work through steps to make the user selected drink:
      - verify inventory
      - get coins
      - verify enough coins
      - update inventory (actually make the drink)
      - calculate user change
      - present drink and change

    Args:
        drink (str): user selected drink
        inventory (dict): machine inventory

    Returns:
        inventory: machine inventory
    """
    if sufficient_inventory(drink, inventory):

        coins = get_coins()
        total_money = sum_coins(coins)
        if not sufficient_money(drink, total_money):
            print("Sorry that's not enough money. Money refunded.")
            return inventory
        inventory = update_inventory(drink, inventory)
        change = calculate_change(total_money, drink)
        present_drink_and_change(drink, change)

    return inventory


def make_cappuccino(inventory, *args, **kwargs):
    """call "make drink" for cappuccino

    Args:
        inventory (dict): machine inventory

    Returns:
        dict: machine inventory
    """
    return make_drink("cappuccino", inventory)


def make_espresso(inventory, *args, **kwargs):
    """call "make drink" for Espresso

    Args:
        inventory (dict): machine inventory

    Returns:
        dict: machine inventory
    """
    return make_drink("espresso", inventory)


def make_latte(inventory, *args, **kwargs):
    """call "make drink" for Latte

    Args:
        inventory (dict): machine inventory

    Returns:
        dict: machine inventory
    """
    return make_drink("latte", inventory)


def present_drink_and_change(drink, change):
    """print messages for made drink and user change

    Args:
        drink (str): selected drink
        change (float): change after making drink
    """
    print(f"Here is your {drink}, Enjoy!")
    if change > 0:
        print(f"Here is ${change:.2f} in change")


def print_report(inventory, *args, **kwargs):
    """print machine inventory report

    Args:
        inventory (dict): dictionary contaning machine inventory

    Return:
        dict: machine inventory
    """
    # for k, v in inventory.items():
    #     print(f"{k}: {v}")
    print(f"Water: {inventory['water']}ml")
    print(f"Milk: {inventory['milk']}ml")
    print(f"Coffee: {inventory['coffee']}g")
    print(f"Money: ${inventory['money']:.2f}")
    return inventory


def sufficient_money(drink, money):
    """Check if deposited money is sufficient to buy drink, return boolean

    Args:
        drink (str): drink selected
        money (float): money inserted

    Returns:
        boolean: True if enough money deposited
    """
    return money >= MENU[drink]["cost"]


def sufficient_inventory(drink, inventory):
    """check if machine has sufficient inventory for sslected drink

    Args:
        drink (str): selected drink
        inventory (dict): machine inventory

    Returns:
        bool: true if machine has sufficient inventory
    """
    sufficient = True
    for ingredient, required in MENU[drink]["ingredients"].items():
        if required > inventory[ingredient]:
            sufficient = False
            print(f"Sorry there is not enough {ingredient}")
    return sufficient


def sum_coins(coins):
    """loop trough coins entered, add up and return total

    Args:
        coins (dict): dictionary of coin types and quantities

    Returns:
        float: float of total dollar value
    """
    total = 0
    for coin, qty in coins.items():
        total += COIN_VALUES[coin] * qty
    return total


def system_off(*args, **kwargs):
    """print shutdown message and return shutdown
    accept inputs without errors as *args and **kwargs but disregard

    Returns:
        str: return shutdown
    """
    print("System shutdown")
    return "shutdown"


def update_inventory(drink, inventory):
    """remove items from inventory required to make the drink

    Args:
        drink (str): drink selected
        inventory (dict): machine inventory

    Returns:
        dict: updated inventory
    """
    for item, ammount in MENU[drink]["ingredients"].items():
        inventory[item] -= ammount
    inventory["money"] += MENU[drink]["cost"]
    return inventory


inventory = {
    "water": 1000,  # amount of water in ml
    "milk": 1000,  # amount of milk in ml
    "coffee": 1000,  # amount of coffee in g
    "money": 0.00,  # TODO change to track specific coins maybe?
}

machine_is_on = True

selections = {
    "espresso": make_espresso,
    "latte": make_latte,
    "cappuccino": make_cappuccino,
    "report": print_report,
    "off": system_off,
}

while machine_is_on:

    # Prompt user for input
    action = get_valid_input(
        "What would you like? (espresso/latte/cappuccino): ",
        selections.keys(),
    )

    result = selections[action](inventory)

    if result == "shutdown":
        machine_is_on = False
    else:
        inventory = result
