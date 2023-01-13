from project.animals.animal import Mammal
from project.food import Vegetable, Fruit, Meat


class Mouse(Mammal):
    def make_sound(self):
        return "Squeak"

    def feed(self, type_of_food):
        if isinstance(type_of_food, Vegetable) or isinstance(type_of_food, Fruit):
            self.food_eaten += type_of_food.quantity
            self.weight += type_of_food.quantity * 0.10
        else:
            return f"{self.__class__.__name__} does not eat {type_of_food.__class__.__name__}!"

class Dog(Mammal):
    def make_sound(self):
        return "Woof!"

    def feed(self, type_of_food):
        if isinstance(type_of_food, Meat):
            self.food_eaten += type_of_food.quantity
            self.weight += type_of_food.quantity * 0.40
        else:
            return f"{self.__class__.__name__} does not eat {type_of_food.__class__.__name__}!"


class Cat(Mammal):
    def make_sound(self):
        return "Meow"

    def feed(self, type_of_food):
        if isinstance(type_of_food, Vegetable) or isinstance(type_of_food, Meat):
            self.food_eaten += type_of_food.quantity
            self.weight += type_of_food.quantity * 0.30
        else:
            return f"{self.__class__.__name__} does not eat {type_of_food.__class__.__name__}!"


class Tiger(Mammal):
    def make_sound(self):
        return "ROAR!!!"

    def feed(self, type_of_food):
        if isinstance(type_of_food, Meat):
            self.food_eaten += type_of_food.quantity
            self.weight += type_of_food.quantity * 1.00
        else:
            return f"{self.__class__.__name__} does not eat {type_of_food.__class__.__name__}!"



