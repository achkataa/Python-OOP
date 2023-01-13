from project.astronaut.astronaut_repository import AstronautRepository
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.planet.planet import Planet
from project.planet.planet_repository import PlanetRepository

class AstronautFactory:
    def create(self, astronaut_type, name):
        if astronaut_type == "Biologist":
            return Biologist(name)
        elif astronaut_type == "Geodesist":
            return Geodesist(name)
        elif astronaut_type == "Meteorologist":
            return Meteorologist(name)
        else:
            return None

class SpaceStation:
    successful_missions = 0
    unsuccessful_missions = 0
    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()

    def add_astronaut(self, astronaut_type: str, name: str):
        astronaut = AstronautFactory().create(astronaut_type, name)
        if astronaut == None:
            raise Exception("Astronaut type is not valid!")
        if self.astronaut_repository.find_by_name(name):
            return f"{name} is already added."
        self.astronaut_repository.add(astronaut)
        return f"Successfully added {astronaut_type}: {name}."

    def add_planet(self, name: str, items: str):
        planet = Planet(name)
        if self.planet_repository.find_by_name(name):
            return f"{name} is already added."
        planet.items = items.split(", ")
        self.planet_repository.add(planet)
        return f"Successfully added Planet: {name}."

    def retire_astronaut(self, name: str):
        astronaut = self.astronaut_repository.find_by_name(name)
        if astronaut == None:
            raise Exception(f"Astronaut {name} doesn't exist!")
        self.astronaut_repository.remove(astronaut)
        return f"Astronaut {name} was retired!"

    def recharge_oxygen(self):
        for a in self.astronaut_repository.astronauts:
            a.increase_oxygen(10)

    def pick_astronauts(self):
        return sorted([x for x in self.astronaut_repository.astronauts if x.oxygen > 30], key=lambda x: x.oxygen, reverse=True)[0:5]

    def send_on_mission(self, planet_name: str):
        planet = self.planet_repository.find_by_name(planet_name)
        if planet == None:
            raise Exception("Invalid planet name!")
        suitable_astronauts = self.pick_astronauts()
        if not suitable_astronauts:
            raise Exception("You need at least one astronaut to explore the planet!")

        participants = 0

        for a in suitable_astronauts:
            if not planet.items:
                break
            while planet.items and a.oxygen > 0:
                item = planet.items.pop()
                a.backpack.append(item)
                a.breathe()
            participants += 1

        if not planet.items:
            self.successful_missions += 1
            return f"Planet: {planet_name} was explored. {participants} astronauts participated in collecting items."
        self.unsuccessful_missions += 1
        return "Mission is not completed."



    def report(self):
        result = ""
        result += f"{self.successful_missions} successful missions!\n"
        result += f"{self.unsuccessful_missions} missions were not completed!\n"
        for a in self.astronaut_repository.astronauts:
            result += f"{repr(a)}"
        return result


