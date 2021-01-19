from turtle import Turtle, Screen
from random import randint  # , choice

timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("chartreuse3")
# timmy.forward(100)
# timmy.right(90)

screen = Screen()
screen.colormode(255)

# Challenge 1 - Draw a square
# for _ in range(4):
#     timmy.forward(100)
#     timmy.right(90)


# Challenge 2 - draw a dashed line
# for _ in range(15):
#     timmy.pendown()
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)

# Challenge 3 - Draw Triangle, square, pentagon, hexagon, heptagon,
# octagon, nonagon and decagon, each with site len 100 and random color

# instructor did most of this in a function and looped over function

# for colors instructor built a list of pre-picked colours and random
# choose from list

# for sides in range(3, 11):
#     angle = 360 / sides
#     r = randint(0, 255)
#     g = randint(0, 255)
#     b = randint(0, 255)
#     timmy.color((r, g, b))
#     for _ in range(sides):
#         timmy.right(angle)
#         timmy.forward(100)

# Challenge 4 - draw a random walk
# def random_color():
#     r = randint(0, 255)
#     g = randint(0, 255)
#     b = randint(0, 255)
#     return (r, g, b)


# angles = [0, 90, 180, 270]
# timmy.pensize(10)
# timmy.speed(10)
# for _ in range(500):
#     rgb = random_color()
#     timmy.color(rgb)
#     # timmy.right(choice(angles))  # changed this after watching instructor
#     timmy.setheading(choice(angles))
#     timmy.forward(50)


# Challenge 5 - Draw a spirograph with
def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return (r, g, b)


timmy.speed(0)
# instructor does `range(int(360/size))`
for heading in range(0, 360, 5):
    timmy.color(random_color())
    timmy.setheading(heading)
    timmy.circle(100)


screen.exitonclick()
