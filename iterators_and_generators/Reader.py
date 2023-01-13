def read_next(*args):
    for iterable in args:
        for x in iterable:
            yield x


for item in read_next('string', (2,), {'d': 1, 'i': 2, 'c': 3, 't': 4}):
    print(item, end='')

