from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.decoration.decoration_repository import DecorationRepository
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish


class AquariumFactory:
    def create(self, aquarium_type, aquarium_name):
        if aquarium_type == "FreshwaterAquarium":
            return FreshwaterAquarium(aquarium_name)
        elif aquarium_type == "SaltwaterAquarium":
            return SaltwaterAquarium(aquarium_name)
        else:
            return None

class DecorationFactory:
    def create(self, decoration_type):
        if decoration_type == "Ornament":
            return Ornament()
        elif decoration_type == "Plant":
            return Plant()
        else:
            return None

class FishFactory:
    def create(self, fish_type, fish_name, fish_species, price):
        if fish_type == "FreshwaterFish":
            return FreshwaterFish(fish_name, fish_species, price)
        elif fish_type == "SaltwaterFish":
            return SaltwaterFish(fish_name, fish_species, price)
        else:
            return None



class Controller:
    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums = []
        self.aquarium_names = []

    def add_aquarium(self, aquarium_type: str, aquarium_name: str):
        aquarium = AquariumFactory().create(aquarium_type, aquarium_name)
        if aquarium == None:
            return "Invalid aquarium type."
        self.aquariums.append(aquarium)
        self.aquarium_names.append(aquarium_name)
        return f"Successfully added {aquarium_type}."


    def add_decoration(self, decoration_type: str):
        decoration = DecorationFactory().create(decoration_type)
        if decoration == None:
            return "Invalid decoration type."
        self.decorations_repository.add(decoration)
        return f"Successfully added {decoration_type}."

    def find_aquarium(self, aquarium_name):
        return [aq for aq in self.aquariums if aq.name == aquarium_name][0]

    def insert_decoration(self, aquarium_name: str, decoration_type: str):
        if aquarium_name in self.aquarium_names:
            aquarium = self.find_aquarium(aquarium_name)
            decoration = self.decorations_repository.find_by_type(decoration_type)
            if decoration == "None":
                return f"There isn't a decoration of type {decoration_type}."
            aquarium.add_decoration(decoration)
            return f"Successfully added {decoration_type} to {aquarium_name}."



    def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float):
        fish = FishFactory().create(fish_type, fish_name, fish_species, price)
        if fish == None:
            return f"There isn't a fish of type {fish_type}."
        if aquarium_name in self.aquarium_names:
            aquarium = self.find_aquarium(aquarium_name)
            if len(aquarium.fish) >= aquarium.capacity:
                return "Not enough capacity."
            if not fish.allowed_aquarium == aquarium.__class__.__name__:
                return "Water not suitable."
            aquarium.add_fish(fish)
            return f"Successfully added {fish_type} to {aquarium_name}."


    def feed_fish(self, aquarium_name: str):
        aquarium = self.find_aquarium(aquarium_name)
        aquarium.feed()
        return f"Fish fed: {len(aquarium.fish)}"

    def calculate_value(self, aquarium_name: str):
        aquarium = self.find_aquarium(aquarium_name)
        total_sum = aquarium.sum_fish_price + aquarium.sum_decorations_price
        return f"The value of Aquarium {aquarium_name} is {total_sum:.2f}."


    def report(self):
        result = ""
        for aq in self.aquariums:
            result += f"{str(aq)}\n"
        return result