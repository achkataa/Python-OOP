from abc import ABC, abstractmethod

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade



class Formatter(ABC):
    @abstractmethod
    def format(self, student: Student):
        pass


class FormatNameAndAge(Formatter):
    def format(self, student: Student):
        return f"{student.name} - {student.age} --- registered"


class FormatNameAndAgeAndGrade(Formatter):
    def format(self, student: Student):
        return f"{student.name} - {student.age} - {student.grade} --- registered"


class StudentRegistry:
    def __init__(self):
        self.db = []
    def register_student(self, student: Student, formatter: Formatter):
        self.db.append(formatter.format(student))
        return formatter.format(student)

    def return_db(self):
        return self.db


st1 = Student("Ivan", 16, 5.40)
print(StudentRegistry().register_student(st1, FormatNameAndAge()))
print(StudentRegistry().register_student(st1, FormatNameAndAgeAndGrade()))

print(StudentRegistry().return_db())