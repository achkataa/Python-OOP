# def values_gen(n):
#     value = 0
#     while value <= n:
#         yield value
#         value += 1
#
#
# class ValuesGen:
#     def __init__(self, n):
#         self.n = n
#
#     def __iter__(self):
#         value = 1
#         while value <= self.n:
#             yield value
#             value += 1
#
#
#
# gen = ValuesGen(5)
#
# for x in gen:
#     print(x)

#
# gen = (x for x in range(1, 11))
# print(list(gen))


def gen():
    return (x for x in range(5))


for x in gen():
    print(x)