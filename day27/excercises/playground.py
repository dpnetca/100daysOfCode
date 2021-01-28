# def add(*args):
#     return sum(args)


# print(add(1, 2, 3, 5, 6, 7, 8, 9, 1298723))


class Car:
    def __init__(self, **kwargs) -> None:
        self.model = kwargs.get("model")
        self.make = kwargs.get("make")


my_car = Car(make="Nissan")
print(my_car.make)
print(my_car.model)
