from turtle import Turtle

OFFSET = 20


class Paddle:
    def __init__(self, x_pos, paddle_width=3):
        self.segments = []
        y_pos = (paddle_width // 2) * OFFSET
        for _ in range(paddle_width):
            position = (x_pos, y_pos)
            new_segment = Turtle(shape="square")
            new_segment.penup()
            new_segment.color("white")
            new_segment.goto(position)
            self.segments.append(new_segment)
            y_pos -= OFFSET
        self.top_segment = self.segments[0]
        self.bottom_segment = self.segments[-1]
        self.top_segment.setheading(90)
        self.bottom_segment.setheading(270)
        self.top_segment.color("red")
        self.bottom_segment.color("green")

    def up(self):
        if self.top_segment.ycor() < 280:
            for seg_num in range(len(self.segments) - 1, 0, -1):
                self.segments[seg_num].goto(
                    self.segments[seg_num - 1].position()
                )
            self.top_segment.forward(20)

    def down(self):
        if self.bottom_segment.ycor() > -280:
            for seg_num in range(len(self.segments) - 1):
                self.segments[seg_num].goto(
                    self.segments[seg_num + 1].position()
                )
            self.bottom_segment.forward(20)
