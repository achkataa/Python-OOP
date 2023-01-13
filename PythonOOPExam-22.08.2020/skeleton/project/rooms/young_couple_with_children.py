from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.tv import TV
from project.rooms.room import Room


class YoungCoupleWithChildren(Room):
    room_cost = 30
    def __init__(self, family_name: str, salary_one: float, salary_two: float, *children):
        members_count = 2+len(children)
        super().__init__(family_name, salary_one + salary_two, members_count)
        self.children = list(children)
        self.appliances = self.generate_appliances()
        self.calculate_expenses(self.appliances, self.children)

    def generate_appliances(self):
        appliances = []
        for x in range(self.members_count):
            appliances.append(TV())
            appliances.append(Fridge())
            appliances.append(Laptop())
        return appliances