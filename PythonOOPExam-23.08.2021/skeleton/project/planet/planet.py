class Planet:
    def __init__(self, name: str):
        self.name = name
        self.items = []

    def validate_name(self, value):
        if value.strip() == "":
            raise ValueError("Planet name cannot be empty string or whitespace!")

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.validate_name(value)
        self.__name = value



