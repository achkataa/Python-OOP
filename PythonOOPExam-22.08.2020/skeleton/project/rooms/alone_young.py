from project.appliances.tv import TV
from project.rooms.room import Room
from typing import List


class AloneYoung(Room):
    room_cost = 10
    appliances: List[TV] = [TV()]
    def __init__(self, family_name: str, salary: float):
        super().__init__(family_name, salary, 1)
        self.calculate_expenses(self.appliances)






