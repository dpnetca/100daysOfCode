from turtle import Turtle


class Router(Turtle):
    def __init__(self, position):
        super().__init__()
        self._position = position
        self.draw_router()

    def draw_router(self):
        self.clear()
        x, y = self._position
        self.penup()
        self.goto(x, y)
        self.dot(50, "blue")
        self.hideturtle()
        self.shapesize(stretch_wid=2, stretch_len=2)
        self.color("white")
        self.goto(x, y - 30)
        self.write("X", align="center", font=("arial", 35, "normal"))
        self.goto(x, y)
