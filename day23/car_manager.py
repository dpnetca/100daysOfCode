import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        """
        initialize car manager, seed screen with the minimum number of cars
        placed randomly along the Y axis, and on the right hand side of the
        X Axis
        """
        self.cars = []
        self.max_cars = 30
        self.min_cars = 10
        self.chance = 5
        self.move_distance = STARTING_MOVE_DISTANCE
        self._seed_initial_cars()

    def _seed_initial_cars(self):
        """
        randomly palce initial cars
        """
        for _ in range(self.min_cars):
            self._create_car(random.randint(0, 300))

    def _create_car(self, x_pos=300):
        """Create a 20 x 40 car with a random color, and random y axis
        start position.

        """
        new_car = Turtle(shape="square")
        new_car.penup()
        new_car.shapesize(stretch_len=2, stretch_wid=1)
        new_car.color(random.choice(COLORS))
        new_car.setheading(180)
        good_position = False
        while not good_position:
            y_pos = random.randint(-250, 250)
            new_car.goto(x_pos, y_pos)
            # Enssure minimum seperateion between cars
            good_position = True
            for car in self.cars:
                if car.distance(new_car) < 45:
                    good_position = False

        self.cars.append(new_car)

    def is_collision(self, collision_object):
        """
        Get the X and Y coordinates of the colission object, and x and y size
        build a set with all whole numnbers between x coners and y corners
        if shape is a turtle add 5 extra to top of y to account for head
        note this uses set comprehension which is not yet taught, could
        also be done with a for loop...


        For each car in the car list
        Get the X and Y coordinates of the car and it's x and y size
        build a set with all whole numnbers between x coners and y corners

        check for intersection between obect on X and Y axis, if there
        is intersection on BOTH axism then object is collided

        """
        x_pos = int(collision_object.xcor())
        y_pos = int(collision_object.ycor())
        x_size, y_size, _ = collision_object.shapesize()
        x_offset = int(x_size * 10)
        y_offset = int(y_size * 10)
        if collision_object.shape() == "turtle":
            y_head = 5
        else:
            y_head = 0
        obj_x = {x for x in range(x_pos - x_offset, x_pos + x_offset)}
        obj_y = {y for y in range(y_pos - y_offset, y_pos + y_offset + y_head)}
        for car in self.cars:
            x_pos = int(car.xcor())
            y_pos = int(car.ycor())
            x_size, y_size, _ = collision_object.shapesize()
            x_offset = int(x_size * 10)
            y_offset = int(y_size * 10)
            car_x = {x for x in range(x_pos - x_offset, x_pos + x_offset)}
            car_y = {y for y in range(y_pos - y_offset, y_pos + y_offset)}
            x_overlap = car_x & obj_x
            y_overlap = car_y & obj_y

            if len(x_overlap) > 1 and len(y_overlap) > 1:
                return True
        return False

    def maybe_create_car(self):
        """
        ensure there are a minimum number of cars on screen at all times
        if there are less then minimum, add a nother car
        otherwise randomly add a car as long as we don't have max cars
        on screen
        """
        if len(self.cars) < self.max_cars:
            if (
                len(self.cars) < self.min_cars
                or random.randint(0, self.chance) == 0
            ):
                self._create_car()

    def move_cars(self):
        """
        move each car forward a set distance
        """
        for car in self.cars:
            car.forward(self.move_distance)

    def purge_cars(self):
        """
        Once cars get off screen hide them and remove them from list
        """
        new_cars = []
        for car in self.cars:
            if car.xcor() > -320:
                new_cars.append(car)
            else:
                car.hideturtle()
        self.cars = new_cars

    def level_up(self):
        """
        speed up cars
        """
        self.move_distance += MOVE_INCREMENT
