import random
from turtle import Turtle

COLORS = ["red", "green", "purple"]


class Packets:
    def __init__(self, routers):
        self.packets = []
        self.routers = routers
        self.start_position = self.routers[0].position()

    def create_packet(self):
        new_packet = Turtle(shape="square")
        new_packet.penup()
        new_packet.color(random.choice(COLORS))
        new_packet.goto(self.start_position)
        new_packet.shapesize(stretch_len=0.4, stretch_wid=0.4)

        self.packets.append(new_packet)

    def move(self):
        new_packets = []
        for packet in self.packets:
            at_final_router = False
            for router in self.routers[-1]:
                if packet.distance(router) < 10:
                    at_final_router = True
            if at_final_router:
                packet.hideturtle()
            else:
                packet.forward(10)
                new_packets.append(packet)

        self.packets = new_packets

    def route(self):
        for packet in self.packets:
            for i in range(len(self.routers) - 1):
                if packet.distance(self.routers[i]) < 10:
                    if isinstance(self.routers[i + 1], list):
                        destination = random.choice(self.routers[i + 1])
                    else:
                        destination = self.routers[i + 1]
                    packet.setheading(packet.towards(destination))
