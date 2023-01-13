from abc import ABC, abstractmethod


class Astronaut(ABC):
    @abstractmethod
    def __init__(self, name: str, oxygen: int):
        self.name = name
        self.oxygen = oxygen
        self.backpack = []

    def validate_name(self, value):
        if value.strip() == "":
            raise ValueError("Astronaut name cannot be empty string or whitespace!")

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.validate_name(value)
        self.__name = value

    def breathe(self):
        self.oxygen -= 10

    def increase_oxygen(self, amount: int):
        self.oxygen += amount

    def __repr__(self):
        backpack = ', '.join(self.backpack)
        return f"Name: {self.name}\n" \
               f"Oxygen: {self.oxygen}\n" \
               f"Backpack items: {backpack if backpack else 'none'}\n"





