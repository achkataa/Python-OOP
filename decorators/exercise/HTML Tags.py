def tags(tag):
    def decorator(func):
        def wrapper(*args):
            return f"<{tag}>{func(*args)}</{tag}>"

        return wrapper

    return decorator

@tags("p")
def return_message(message):
    return message


print(return_message("Hello"))

