# ll = [1, 2, 3, 4, 5, 6, 7, 8]
#
# ll_iter = iter(ll)
# print(next(ll_iter))
# print(next(ll_iter))
# print(next(ll_iter))
# print(next(ll_iter))
# print(next(ll_iter))

#
# while True:
#     try:
#         print(next(ll_iter))
#     except StopIteration:
#         break
#

# class CustomRange:
#     def __init__(self, start, end):
#         self.start = start
#         self.end = end
#
#     def __iter__(self):
#         return self.iterator(self)
#
#     def __reversed__(self):
#         return self.iterator(self, is_reversed=True)
#
#     class iterator:
#         def __init__(self, custom_range_object, is_reversed=False):
#             self.custom_range_object = custom_range_object
#             self.is_reversed = is_reversed
#             if not self.is_reversed:
#                 self.value = self.custom_range_object.start
#             else:
#                 self.value = self.custom_range_object.end
#
#         def __iter__(self):
#             return self
#
#         def __next__(self):
#             if self.value > self.custom_range_object.end or self.value < self.custom_range_object.start:
#                 raise StopIteration
#
#             value = self.value
#             if self.is_reversed:
#                 self.value -= 1
#             else:
#                 self.value += 1
#             return value
#
# cr = CustomRange(1, 10)
#
# for x in cr:
#     print(f"Iter1: {x}")
#
# for x in cr:
#     print(f"Iter2: {x}")
#
# for x in reversed(cr):
#     print(f"reversed: {x}")

#
# a = [1, 2, 3, 4]
#
# a = iter(a)
#
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))


class custom_range:
    def __init__(self, end):
        self.end = end
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num > self.end:
            raise StopIteration

        num = self.num
        self.num += 1
        return num



iterA = custom_range(5)
iterB = custom_range(5)

print(next(iterA))
print(next(iterA))
print(next(iterB))





# for x in custom_range(5):
#     print(x)