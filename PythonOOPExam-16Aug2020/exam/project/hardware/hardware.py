from project.software.software import Software
from typing import List


class Hardware:
    def __init__(self, name: str, hardware_type: str, capacity: int, memory: int):
        self.name = name
        self.hardware_type = hardware_type
        self.capacity = capacity
        self.memory = memory
        self.software_components: List[Software] = []

    def install(self, software: Software):
        if self.available_capacity >= software.capacity_consumption and self.available_memory >= software.memory_consumption:
            self.software_components.append(software)
        else:
            raise Exception("Software cannot be installed")

    def uninstall(self, software: Software):
        if software in self.software_components:
            self.software_components.remove(software)

    
    @property
    def available_capacity(self):
        return self.capacity - self.total_capacity_used

    @property
    def available_memory(self):
        return self.memory - self.total_memory_used

    @property
    def total_capacity_used(self):
        return sum([s.capacity_consumption for s in self.software_components])

    @property
    def total_memory_used(self):
        return sum([s.memory_consumption for s in self.software_components])


