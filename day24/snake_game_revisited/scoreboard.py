from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Comic Sans MS", 22, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.read_high_score()
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(
            f"Score:  {self.score}  High Score: {self.high_score}",
            align=ALIGNMENT,
            font=FONT,
        )

    def increase_score(self):
        self.score += 1
        self.update_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.write_high_score()
        self.score = 0
        self.update_score()

    def read_high_score(self):
        with open("data.txt") as f:
            self.high_score = int(f.read())

    def write_high_score(self):
        with open("data.txt", "w") as f:
            f.write(str(self.high_score))
