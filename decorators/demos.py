# def calculator():
#     result = 0
#
#     def add(x):
#         nonlocal result
#         result += x
#
#     def multiply(x):
#         nonlocal result
#         result *= x
#
#     def get_result():
#         return result
#
#     return (add, multiply, get_result)
#
#
# (add1, multiply1, get_result1) = calculator()
# (add2, multiply2, get_result2) = calculator()
#
# add1(1)
# print(get_result1())
# print(get_result2())
# add2(3)
# print(get_result2())

#
# def uppercase_decorator(func):
#     def wrapper(*args, **kwargs):
#         return func(*args, **kwargs).upper()
#
#     return wrapper
#
#
# @uppercase_decorator
# def get_hello_message(name):
#     return f"Hello, I am {name}"
#
# @uppercase_decorator
# def get_temperature(degrees):
#     return f"The temperature is {degrees} degrees celsius "
#
# print(get_hello_message("Gosho"))
# print(get_temperature(15))




# from datetime import datetime
#
#
# def measure_time_decorator(func):
#     def wrapper():
#         start = datetime.now()
#         func()
#         end = datetime.now()
#         return (f"func {func.__name__} executed for {end - start}")
#
#     return wrapper
#
#
# @measure_time_decorator
# def big_loop():
#     x = 0
#     for _ in range(100000000):
#         x += 1
#
# print(big_loop())
# import functools
#
# def repeat(count):
#     def decorator(func):
#         functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             result = None
#             for _ in range(count):
#                 result = func(*args, **kwargs)
#             return result
#         return wrapper
#     return decorator
#
#
#
#
# @repeat(5)
# def print_message(name):
#     print(f"Hello I am {name}")
#
#
# print_message("Gosho")
# import functools
#
#
# def upper(func):
#     functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         return func(*args, **kwargs).upper()
#     return wrapper
#
#
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     @upper
#     def say_hi(self):
#         return f"Hello I am {self.name} - {self.age} years old"
#
#
# prs = Person("Gosho", 15)
# print(prs.say_hi())



def print_message():
    print("Hello")


print_message()
