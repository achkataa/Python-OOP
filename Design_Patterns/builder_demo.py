from abc import ABC, abstractmethod


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"I am {self.name} --- {self.age} years old"


person = Person("Gosho", 20)


class Logger(ABC):
    def __init__(self, file=None):
        self.file = file
    @abstractmethod
    def log(self, obj):
        pass


class FileLogger(Logger):
    def __init__(self, file):
        super().__init__(file)

    def log(self, obj):
        with open(self.file, "a") as file:
            file.write(str(obj))


class ConsoleLogger(Logger):
    def log(self, obj):
        print(obj)


class LoggersBuilder:
    def __init__(self):
        self.path = None
        self.environment = "prod"

    @property
    def file(self):
        return self.__path
    
    @file.setter
    def file(self, value):
        self.__path = value

    @property
    def environment(self):
        return self.__environment

    @environment.setter
    def environment(self, value):
        self.__environment = value

    def build(self):
        if self.environment == "prod":
            return FileLogger(self.path)
        else:
            return ConsoleLogger()





loggers_builder = LoggersBuilder()
loggers_builder.path = "result.txt"
loggers_builder.build().log(person)

