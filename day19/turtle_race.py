from turtle import Turtle, Screen
from random import randint


screen = Screen()
screen.setup(width=500, height=400)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

valid_bet = False
while not valid_bet:
    user_bet = screen.textinput(
        title="Make your bet",
        prompt="Which turtle will win the race? Enter a color: ",
    ).lower()
    if user_bet in colors:
        valid_bet = True

x_pos = -230
y_offset = 300 / len(colors)
y_pos = -150 + y_offset / 2

turtles = {}
for color in colors:
    turtles[color] = Turtle(shape="turtle")
    turtles[color].penup()
    turtles[color].color(color)
    turtles[color].goto(x=x_pos, y=y_pos)
    y_pos += y_offset

race_is_on = True

while race_is_on:
    at_finish = []
    for turtle_name, turtle in turtles.items():
        turtle.forward(randint(0, 10))
        if turtle.xcor() >= 230:
            at_finish.append(turtle_name)
    if at_finish:
        race_is_on = False

if len(at_finish) > 1:
    print("wow it's almost too close to call, so we'll call it a tie")
    print(f"{','.join(at_finish)} all passed the finish line in the same tick")
elif user_bet in at_finish:
    print(f"You won your bet!! {at_finish[0]} won the race")
else:
    print(f"Sorry, you lost your bet. {at_finish[0]} won the race")

# tim = Turtle(shape="turtle")
# tim.penup()
# tim.goto(x=-230, y=0)
screen.exitonclick()
