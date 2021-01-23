from turtle import Turtle


class Connection(Turtle):
    def __init__(self, obj_a, obj_b):
        super().__init__()
        self.penup()
        self.hideturtle()
        # self.color("black")
        self.goto(obj_a.position())
        self.pensize(5)
        self.pendown()
        self.goto(obj_b.position())
        obj_a.draw_router()
        obj_b.draw_router()
