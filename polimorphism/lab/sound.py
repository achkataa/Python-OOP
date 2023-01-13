class Cat:
    def sound(self):
        return "Meow"


class Dog:
    def sound(self):
        return "Bark"



def make_sound(animal):
    if animal == "Cat":
        return Cat()
    return Dog()


animal = "Dog"
sound = make_sound(animal).sound()
print(sound)