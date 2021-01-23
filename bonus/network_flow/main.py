import time
from turtle import Screen
from router import Router
from connection import Connection
from packets import Packets

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

r1 = Router((-150, 0))
r2 = Router((0, 0))
r3 = Router((150, 75))
r4 = Router((150, -75))

r1_r2 = Connection(r1, r2)
r2_r3 = Connection(r2, r3)
r2_r4 = Connection(r2, r4)

packets = Packets([r1, r2, [r3, r4]])
network_is_on = True
while network_is_on:
    time.sleep(0.1)
    packets.create_packet()
    screen.update()
    packets.move()
    packets.route()


screen.exitonclick()
