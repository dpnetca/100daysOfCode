from turtle import Turtle
import random
import time


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.75, stretch_wid=0.75)
        self.color("white")
        self.start()

    def move(self):
        time.sleep(0.1)
        self.forward(20)

    def start(self):
        self.goto(0, 0)
        self.setheading(random.choice([45, 135, 225, 315]))
        # self.setheading(45)

    def bounce(self, bounce_angle):
        new_heading = bounce_angle - self.heading()
        new_heading = new_heading % 360
        self.setheading(new_heading)

    def check_collission(self, paddles):
        for paddle in paddles:
            if self.is_paddle_collission(paddle):
                self.bounce(180)
        if abs(self.ycor()) > 280:
            self.bounce(360)

    def is_paddle_collission(self, paddle):
        for segment in paddle.segments:
            if self.distance(segment) < 20:
                return True
        return False
