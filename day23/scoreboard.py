from turtle import Turtle

FONT = ("Courier", 24, "normal")
ALIGN = "left"


class Scoreboard(Turtle):
    def __init__(self):
        """
        initialize scoreboard with a level 1
        """
        super().__init__()
        self.score = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self._write_score()

    def _write_score(self):
        """
        write the score to the screen
        """
        self.clear()
        self.write(f"Level: {self.score}", align=ALIGN, font=FONT)

    def level_up(self):
        """
        increasen level and update score on screen
        """
        self.score += 1
        self._write_score()

    def game_over(self):
        """
        print game over message
        """
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
