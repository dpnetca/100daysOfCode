from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Comic Sans MS", 48, "normal")


class Score(Turtle):
    def __init__(self, x_pos):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(x_pos, 200)
        self.color("white")
        self._update_score()

    def _update_score(self):
        self.clear()
        self.write(
            f"{self.score}",
            align=ALIGNMENT,
            font=FONT,
        )

    def increase_score(self):
        self.score += 1
        self._update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(
            "GAME OVER",
            align=ALIGNMENT,
            font=FONT,
        )
