import json
from abc import ABC, abstractmethod

class Parser(ABC):
    @abstractmethod
    def parse(self, obj):
        pass

class JsonParser(Parser):
    def parse(self, obj):
        return f"json: {json.dumps(obj.__dict__)}"

class StringParser(Parser):
    def parse(self, obj):
        return f"str: {str(obj.__dict__)}"

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


def get_parser(format):
    if format == "json":
        return JsonParser()
    elif format == "string":
        return StringParser()

person = Person("Pesho", 20)
format = input()

parser = get_parser(format)
print(parser.parse(person))


