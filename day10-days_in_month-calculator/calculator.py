import art
import sys
import os


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    if n2 == 0:
        print("don't try and divide by 0....")
        sys.exit(1)
    return n1 / n2


def float_or_int(number):
    """take a number in string format if there is a . in the string return
    the numer as a float, if not return the number as an int

    Args:
        number (str): number in string format

    Returns:
        int or float: number in int or float format
    """
    if "." in number:
        return float(number)
    return int(number)


def get_number(question):
    """get user inuput, and check if valid, if not reprompt

    Args:
        question (str): question to be displayed to user

    Returns:
        int or float: valid integer or float number
    """
    valid_result = False
    while not valid_result:
        try:
            number = float_or_int(input(question))
            return number
        except ValueError:
            print("please enter a valid integer or float number")


def calculator():
    print(art.logo)

    operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide,
    }
    more_calculations = True

    num1 = get_number("What's the first number?: ")

    while more_calculations:
        valid_operation = False
        while not valid_operation:
            operation = input(
                f"What operation? ({', '.join(operations.keys())}): "
            )
            if operation in operations.keys():
                valid_operation = True
            else:
                print("Please enter a valid operator from the list")

        num2 = get_number("What's the next number?: ")

        result = operations[operation](num1, num2)
        print(f"{num1} {operation} {num2} = {result}")

        choice = input(
            "Type "
            "'y' for more calulations, "
            "'n' for a new calculator, or "
            "or any other key to exit: "
        ).lower()

        if choice == "y":
            num1 = result
            clear()
            print(f"previous result: {num1}")
        elif choice == "n":
            more_calculations = False
            clear()
            calculator()
        else:
            more_calculations = False


calculator()
