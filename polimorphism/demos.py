# class GrandFather:
#     def __init__(self, name):
#         self.name = name
#
#     def greet(self):
#         return f"I am {self.name}"
#
#
# class Father(GrandFather):
#     def __init__(self, name):
#         super().__init__(name)
#
#
# class Son(Father):
#     def __init__(self, name):
#         super().__init__(name)
#
#
# son = Son("Ivan")
# father = Father("Gosho")
# grandfather = GrandFather("Tosho")
#
# print(isinstance(grandfather, Father))
# print(isinstance(grandfather, object))
#
# print(0)
import json
from abc import  ABC, abstractmethod
# class Animal(ABC):
#     def __init__(self, name):
#         self.name = name
#
#     @abstractmethod
#     def sound(self):
#         pass
#
#
#
# class Dog(Animal):
#     def __init__(self, name):
#         super().__init__(name)
#
#     def sound(self):
#         pass
#
#
# class Cat(Animal):
#     def __init__(self, name):
#         super().__init__(name)
#
#     def sound(self):
#         pass
#
#
#
# dog = Dog("sharo")
# print(dog.sound())

#
# class Serializer(ABC):
#     @abstractmethod
#     def serialize(self, obj):
#         pass
#
# class TextSerializer(Serializer):
#     def serialize(self, obj):
#         return f"{obj}"
#
#
# class JsonSerializer(Serializer):
#     def serialize(self, obj):
#         return json.dumps(obj)
#
#
# def serializer_type(type, subject):
#     if type == "text":
#         return TextSerializer().serialize(subject)
#     return JsonSerializer().serialize(subject)
#
# type = "text"
# subject = 5
# serializer = serializer_type(type, subject)
# print(serializer)



# class Person:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#
#     def __gt__(self, other):
#         return self.salary > other.salary
#
#
# person_1 = Person("Gosho", 2000)
# person_2 = Person("Petq", 1500)
# print(person_1.__gt__(person_2))
#
#
# a = 1
# b = 2
#
# print(a.__add__(b))

#
# class Person:
#     def __init__(self, name, age=10):
#         self.name = name
#         self.age = age
#
#     def __repr__(self):
#         return f"{self.name} - {self.age}"
#
#
# person = Person("Angel")
# person2 = Person("Gosho", 20)
# print(person)
# print(person2)

# print(40 + (-50))


ll = [1, 2, 3, 4]
ll2 = [5, 6, 7, 8]

ll += ll2

print(ll)