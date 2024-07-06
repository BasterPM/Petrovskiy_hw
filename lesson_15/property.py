class House:
    number = 1
    cost = 100
    name = 'House'

    def __init__(self):
        self.number = House.number
        House.number += 1


class Car:
    number = 1
    cost = 40
    name = 'Car'

    def __init__(self):
        self.number = Car.number
        Car.number += 1
