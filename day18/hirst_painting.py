#!/usr/bin/env python

import colorgram
from turtle import Turtle, Screen
from random import choice


def is_white_ish(rgb, threshold=240):
    """
    take in RGB tuple, if the average value for each color is greater
    then the threshold then the color is probably whiteish, so return
    true, otherwise return false
    """
    if sum(rgb) > (threshold * 3):
        return True
    else:
        return False


# colors = colorgram.extract("image.jpg", 15)
colors = colorgram.extract("image2.jpg", 15)
color_list = []
for color in colors:
    rgb = (color.rgb.r, color.rgb.g, color.rgb.b)
    if not is_white_ish(rgb):
        color_list.append(rgb)


# if you don't want to run the RGB selector every time
# color_list = [
#     (202, 164, 109),
#     (150, 75, 49),
#     (223, 201, 135),
#     (52, 93, 124),
#     (172, 154, 40),
#     (140, 30, 19),
#     (133, 163, 185),
#     (198, 91, 71),
#     (46, 122, 86),
#     (72, 43, 35),
#     (145, 178, 148),
# ]


brush = Turtle()
brush.hideturtle()
brush.speed(0)
brush.penup()

screen = Screen()
screen.colormode(255)

# starting coordinates
x = -250
y = -250

for rows in range(10):
    for cols in range(10):
        brush.goto(x, y)
        brush.dot(20, choice(color_list))
        x += 50
    x = -250
    y += 50


screen.exitonclick()
