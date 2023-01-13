from project.animals.animal import Bird
from project.food import Meat


class Owl(Bird):
    def make_sound(self):
        return "Hoot Hoot"

    def feed(self, type_of_food):
        if isinstance(type_of_food, Meat):
            self.food_eaten += type_of_food.quantity
            self.weight += type_of_food.quantity * 0.25
        else:
            return f"{self.__class__.__name__} does not eat {type_of_food.__class__.__name__}!"


class Hen(Bird):
    def make_sound(self):
        return "Cluck"

    def feed(self, type_of_food):
        self.food_eaten += type_of_food.quantity
        self.weight += type_of_food.quantity * 0.35
