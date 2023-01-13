class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"I am {self.name} --- {self.age} years old"


person = Person("Gosho", 20)


def encrypted(func):
    def wrapper(self, obj):
        return func(self, f"$$${obj}$$$")
    return wrapper

class FileLogger:
    def __init__(self, file):
        self.file = file

    @encrypted
    def log(self, obj):
        with open(self.file, "a") as file:
            file.write(str(obj))


logger = FileLogger("result.txt")
logger.log(person)

