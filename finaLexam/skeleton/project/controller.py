from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar
from project.driver import Driver
from project.race import Race


class CarFactory:
    def create(self, car_type, model, speed_limit):
        if car_type == "MuscleCar":
            return MuscleCar(model, speed_limit)
        if car_type == "SportsCar":
            return SportsCar(model, speed_limit)


class Controller:
    def __init__(self):
        self.cars = []
        self.car_models = []
        self.drivers = []
        self.driver_names = []
        self.races = []
        self.race_names = []

    def create_car(self, car_type: str, model: str, speed_limit: int):
        car = CarFactory().create(car_type, model, speed_limit)
        if car != None:
            if [c for c in self.cars if c.model == model]:
                raise Exception(f"Car {model} is already created!")
            self.cars.append(car)
            self.car_models.append(model)
            return f"{car_type} {model} is created."

    def create_driver(self, driver_name: str):
        driver = Driver(driver_name)
        if [d for d in self.drivers if d.name == driver_name]:
            raise Exception(f"Driver {driver_name} is already created!")
        self.drivers.append(driver)
        self.driver_names.append(driver_name)
        return f"Driver {driver_name} is created."

    def create_race(self, race_name: str):
        race = Race(race_name)
        if [r for r in self.races if r.name == race_name]:
            raise Exception(f"Race {race_name} is already created!")
        self.races.append(race)
        self.race_names.append(race_name)
        return f"Race {race_name} is created."

    def find_driver(self, driver_name):
        return [driver for driver in self.drivers if driver.name == driver_name][0]

    def get_car(self, car_type):
        cars = [car for car in self.cars if car.__class__.__name__ == car_type and car.is_taken == False]
        if not cars:
            raise Exception(f"Car {car_type} could not be found!")
        return cars[-1]

    def add_car_to_driver(self, driver_name: str, car_type: str):
        if not driver_name in self.driver_names:
            raise Exception(f"Driver {driver_name} could not be found!")
        car = self.get_car(car_type)
        driver = self.find_driver(driver_name)
        if driver.car != None:
            old_car = driver.car
            driver.car.is_taken = False
            driver.car = car
            car.is_taken = True
            return f"Driver {driver_name} changed his car from {old_car.model} to {car.model}."
        driver.car = car
        car.is_taken = True
        return f"Driver {driver_name} chose the car {car.model}."

    def find_race(self, race_name):
        return [race for race in self.races if race.name == race_name][0]

    def add_driver_to_race(self, race_name: str, driver_name: str):
        if not race_name in self.race_names:
            raise Exception(f"Race {race_name} could not be found!")
        if not driver_name in self.driver_names:
            raise Exception(f"Driver {driver_name} could not be found!")

        race = self.find_race(race_name)
        driver = self.find_driver(driver_name)

        if driver.car == None:
            raise Exception(f"Driver {driver_name} could not participate in the race!")

        if driver in race.drivers:
            return f"Driver {driver_name} is already added in {race_name} race."

        race.drivers.append(driver)
        return f"Driver {driver_name} added in {race_name} race."


    def start_race(self, race_name: str):
        if race_name not in self.race_names:
            raise Exception(f"Race {race_name} could not be found!")

        race = self.find_race(race_name)

        if len(race.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")

        sorted_drivers = sorted(race.drivers, key=lambda x: x.car.speed_limit, reverse=True)[0:3]

        result = []

        for driver in sorted_drivers:
            driver.number_of_wins += 1
            result.append(f"Driver {driver.name} wins the {race_name} race with a speed of {driver.car.speed_limit}.")

        return '\n'.join(result)

