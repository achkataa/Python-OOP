def singleton(cls):
    instance = None
    def wrapper(*args, **kwargs):
        nonlocal instance
        if not instance:
            instance = cls(*args, **kwargs)
        return instance
    return wrapper


class JsonParser:
    def parse(self, obj):
        return f"json: {str(obj)}"

@singleton
class JsonParser2:
    def parse(self, obj):
        return f"json: {str(obj)}"

jp11 = JsonParser()
jp12 = JsonParser()

jp21 = JsonParser2()
jp22 = JsonParser2()

print(jp11)
print(jp12)
print(jp21)
print(jp22)