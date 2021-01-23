from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        """
        Initialize Turtle
        """
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.restart()

    def move(self):
        """
        move forward set amount
        """
        self.forward(MOVE_DISTANCE)

    def restart(self):
        """
        move turtle to starting position
        """
        self.goto(STARTING_POSITION)

    def is_finished(self):
        """
        if current y position is past the y Finish line return true
        """
        return self.ycor() > FINISH_LINE_Y
