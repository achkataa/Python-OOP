from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.controller import Controller

controller = Controller()

fwa = FreshwaterAquarium("fresh")
controller.add_decoration("Ornament")
controller.add_decoration("Plant")
controller.add_aquarium("FreshwaterAquarium", "top aquarium")
controller.add_aquarium("SaltwaterAquarium", "second aquarium")
controller.add_fish("top aquarium", "FreshwaterFish", "gosho", "hrrr", 10)
controller.add_fish("top aquarium", "FreshwaterFish", "tosho", "hrrr10", 22)
controller.add_fish("second aquarium", "SaltwaterFish", "misho", "hrrr15", 23)
controller.add_fish("second aquarium", "SaltwaterFish", "pesho", "hrrr16", 24)
print(controller.insert_decoration("top aquarium", "Ornament"))
print(controller.insert_decoration("top aquarium", "Plant"))
print(controller.insert_decoration("second aquarium", "Ornament"))
print(controller.insert_decoration("second aquarium", "Plant"))

print(controller.report())


