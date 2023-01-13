from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class AddCommand(Command):
    def __init__(self, values, new_value):
        self.values = values
        self.new_value = new_value

    def execute(self):
        self.values.append(self.new_value)
        return f"{self.new_value} added"


class SumCommand(Command):
    def __init__(self, values):
        self.values = values

    def execute(self):
        return sum(self.values)


class RemoveLastCommand(Command):
    def __init__(self, values):
        self.values = values

    def execute(self):
        num = self.values.pop()
        return f"{num} popped"

command = input()

commands = []
values = [1, 2, 3, 4]

while command != "End":
    if command == "Remove last":
        current_command = RemoveLastCommand(values)
    elif command == "Sum":
        current_command = SumCommand(values)
    else:
        _, value = command.split()
        current_command = AddCommand(values, int(value))
    commands.append(current_command)
    command = input()


for command in commands:
    print(command.execute())
