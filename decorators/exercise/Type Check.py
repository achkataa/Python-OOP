import functools


def type_check(type):
    def decorator(func):
        functools.wraps(func)
        def wrapper(param):
            if not isinstance(param, type):
                return "Bad Type"
            return func(param)


        return wrapper

    return decorator

@type_check(str)
def first_letter(word):
    return word[0]

print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))
