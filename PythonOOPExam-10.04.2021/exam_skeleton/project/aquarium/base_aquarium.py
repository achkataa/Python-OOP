from abc import ABC, abstractmethod


class BaseAquarium(ABC):
    @abstractmethod
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.decorations = []
        self.fish = []

    def validate_name(self, value):
        if value.strip() == "":
            raise ValueError("Aquarium name cannot be an empty string.")

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.validate_name(value)
        self.__name = value
        
    @property
    def sum_fish_price(self):
        return sum([f.price for f in self.fish])

    @property
    def sum_decorations_price(self):
        return sum([d.price for d in self.decorations])



    def calculate_comfort(self):
        return sum([dec.comfort for dec in self.decorations])

    def is_possible_type_fish(self, fish):
        if fish.__class__.__name__ == "SaltwaterFish" or fish.__class__.__name__ == "FreshwaterFish":
            return True
        return False

    def add_fish(self, fish):
        if self.is_possible_type_fish(fish):
            if len(self.fish) < self.capacity:
                self.fish.append(fish)
                return f"Successfully added {fish.__class__.__name__} to {self.name}."
            return "Not enough capacity."

    def remove_fish(self, fish):
        if fish in self.fish:
            self.fish.remove(fish)

    def add_decoration(self, decoration):
        self.decorations.append(decoration)


    def feed(self):
        for f in self.fish:
            f.eat()

    def __str__(self):
        fish = ' '.join(f.name for f in self.fish)
        result = f"{self.name}:\n" \
                 f"Fish: {fish if fish else None}\n" \
                 f"Decorations: {len(self.decorations)}\n" \
                 f"Comfort: {self.calculate_comfort()}"
        return result
