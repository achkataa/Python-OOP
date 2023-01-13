from project.rooms.room import Room


class Everland:
    def __init__(self):
        self.rooms = []

    @property
    def total_people_in_the_hotel(self):
        return sum([room.members_count for room in self.rooms])

    def add_room(self, room: Room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        total_consumption = sum([room.expenses+room.room_cost for room in self.rooms])
        return f"Monthly consumption: {total_consumption}$."

    def pay(self):
        result = []
        for room in self.rooms:
            if room.expenses + room.room_cost <= room.budget:
                room.budget -= (room.expenses + room.room_cost)
                result.append(f"{room.family_name} paid {room.expenses + room.room_cost}$ and have {room.budget}$ left.")
            else:
                self.rooms.remove(room)
                result.append(f"{room.family_name} does not have enough budget and must leave the hotel.")

        return '\n'.join(result)


    def status(self):
        result = ""
        result += f"Total population: {self.total_people_in_the_hotel}\n"
        for room in self.rooms:
            result += f"{room.family_name} with {room.members_count} members. Budget: {room.budget}$, Expenses: {room.expenses}$\n"
            if room.children:
                for child in room.children:
                    result += f"--- Child {room.children.index(child) + 1} monthly cost: {child.get_monthly_expense()}$\n"

            appliances_total_monthly_cost = sum([appliance.get_monthly_expense() for appliance in room.appliances])
            result += f"--- Appliances monthly cost: {appliances_total_monthly_cost}$\n"
        return result