#!/usr/bin/env python


from paddle import Paddle
from ball import Ball
from score import Score
from pong_screen import PongScreen

pong_screen = PongScreen()
screen = pong_screen.screen


p1_paddle = Paddle(x_pos=480)
p2_paddle = Paddle(x_pos=-480)
p1_score = Score(x_pos=40)
p2_score = Score(x_pos=-40)

ball = Ball()

screen.listen()
screen.onkey(p1_paddle.up, "Up")
screen.onkey(p1_paddle.down, "Down")
screen.onkey(p2_paddle.up, "w")
screen.onkey(p2_paddle.down, "s")

game_is_on = True
while game_is_on:
    screen.update()

    ball.move()
    ball.check_collission(paddles=[p1_paddle, p2_paddle])
    if ball.xcor() > 500:
        p2_score.increase_score()
        if p2_score.score >= 5:
            game_is_on = False
            p2_score.game_over()
        ball.start()
    elif ball.xcor() < -500:
        p1_score.increase_score()
        if p1_score.score >= 5:
            game_is_on = False
            p1_score.game_over()
        ball.start()


screen.exitonclick()
