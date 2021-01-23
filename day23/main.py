import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # randomly create new cars
    car_manager.maybe_create_car()

    # move cars forward
    car_manager.move_cars()

    # detect player collision with car
    if car_manager.is_collision(player):
        game_is_on = False
        scoreboard.game_over()

    # remove cars that have left the screen
    car_manager.purge_cars()

    # check if crossed finish line
    if player.is_finished():
        player.restart()
        scoreboard.level_up()
        car_manager.level_up()

screen.exitonclick()
