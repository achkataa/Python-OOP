from project.car.car import Car


class SportsCar(Car):
    def __init__(self, model, speed_limit):
        Car.min_speed_limit = 400
        Car.max_speed_limit = 600
        super().__init__(model, speed_limit)