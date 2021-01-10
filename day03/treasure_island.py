import art

print(art.logo)
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")


print("You have encountered a fork in the road,")
direction = input("do you want to go 'left' or 'right?' ").lower()

if direction == "left":
    print(
        "\nYou encounter a stream, and see a boat approaching in the distance"
    )
    swim_wait = input("would you like to 'swim' or 'wait'? ").lower()

    if swim_wait == "wait":
        print(
            "\nThe boat arrives and takes you across the river where you "
            "encounter three doors."
        )
        door = input(
            "Which door will you take: 'Red', 'Yellow', or 'Blue'? "
        ).lower()

        if door == "yellow":
            print(
                "Winner Winner Chicken Dinner, you found a treasure chest..."
                "full of Chicken"
            )
        elif door == "red":
            print(
                "It's a bird, it's a plane, nope it's arrow coming at your "
                "head - GAME OVER"
            )
        elif door == "blue":
            print(
                "The door locks behind you and traps you in eternal darkness"
                " - GAME OVER"
            )
        else:
            print(
                "you get turned into an Ogre, destined to haunt others who can"
                " not follow instructions - GAME OVER"
            )

    elif swim_wait == "swim":
        print(
            "Oh no, half way across you encounter a hungry Aligator"
            " - GAME OVER"
        )
    else:
        print(
            "A giant ogre magically appears, confused by your invalid answer,"
            " it bops you on the head - GAME OVER "
        )

elif direction == "right":
    print("Oops, you walked off a cliff - GAME OVER")
else:
    print(
        "A giant ogre magically appears and bops you on the head for not"
        " following directions - GAME OVER"
    )
