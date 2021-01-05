# http:reeborg.ca - problem_world.json / problem_world2.json / problem_world3.json


def turn_right():
    turn_left()
    turn_left()
    turn_left()


consecutive_right = 0

while not at_goal():
    if consecutive_right == 4:
        consecutive_right = 0
        if front_is_clear():
            move()
        else:
            turn_left()
    elif right_is_clear():
        turn_right()
        move()
        consecutive_right += 1
    elif front_is_clear():
        move()
        consecutive_right = 0
    else:
        turn_left()
        consecutive_right = 0
