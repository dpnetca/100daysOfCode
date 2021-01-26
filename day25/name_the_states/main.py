#!/usr/bin/env python
import turtle
import pandas

screen = turtle.Screen()
screen.title("US State Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


write_state = turtle.Turtle()
write_state.hideturtle()
write_state.penup()

correct_states = 0

df = pandas.read_csv("50_states.csv")
guessed_states = []

game_on = True
while game_on:
    answer_state = screen.textinput(
        f"{correct_states}/50 States Correct", "What is another state's name? "
    )
    if answer_state.lower() == "quit":
        game_on = False
        continue

    state = df[df.state == answer_state.title()]
    if len(state) == 1:
        write_state.goto(int(state.x), int(state.y))
        write_state.write(answer_state.title())
        # write_state.write(state.state.item())
        correct_states += 1
        guessed_states.append(answer_state.title())

states_to_learn = pandas.DataFrame(columns=["state", "x", "y"])
missing_states = []
for state in df.state:
    if state not in guessed_states:
        missing_states.append(state)

states_to_learn = pandas.DataFrame(missing_states)
states_to_learn.to_csv("states_to_learn.csv")
