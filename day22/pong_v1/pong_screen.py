from turtle import Screen, Turtle


class PongScreen:
    def __init__(self):
        super().__init__()
        self.screen = Screen()
        self.screen.setup(width=1000, height=600)
        self.screen.bgcolor("black")
        self.screen.title("Pong")
        self.screen.tracer(0)
        self.net = Turtle()
        self.net.penup()
        self.net.hideturtle()
        self.net.color("white")
        self.draw_net()

    def draw_net(self):
        self.net.goto((0, 300))
        self.net.setheading(270)
        for _ in range(0, 600, 20):
            self.net.pendown()
            self.net.forward(10)
            self.net.penup()
            self.net.forward(10)
