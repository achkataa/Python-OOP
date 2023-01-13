import functools


def is_valid(args):
    for el in args:
        if not isinstance(el, int) or el % 2 != 0:
            return False
    return True


def even_parameters(func):
    functools.wraps(func)
    def wrapper(*args):
        if not is_valid(args):
            return "Please use only even numbers!"
        return func(*args)

    return wrapper


@even_parameters
def multiply(*nums):
    result = 1
    for num in nums:
        result *= num
    return result

print(multiply(2, 4, 6, 8))
print(multiply(2, 4, 9, 8))

