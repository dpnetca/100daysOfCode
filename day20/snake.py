from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self._create_snake()
        self.head = self.segments[0]

    def _create_snake(self):
        # could make these parameters if we want to allow custom starts
        snake_length = 3
        x_start = 0
        y_start = 0
        x_offset = 20
        for _ in range(snake_length):
            new_segment = Turtle(shape="square")
            new_segment.penup()
            new_segment.color("white")
            new_segment.goto(x=x_start, y=y_start)
            self.segments.append(new_segment)
            x_start -= x_offset

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            self.segments[seg_num].goto(self.segments[seg_num - 1].position())
            # new_position = self.segments[seg_num - 1].position()
            # self.segments[seg_num].goto(new_position)

        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
