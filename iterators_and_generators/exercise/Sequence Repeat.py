# class sequence_repeat:
#     def __init__(self, sequence, number):
#         self.sequence = sequence
#         self.number = number
#         self.index = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.number == 0:
#             raise StopIteration
#
#         self.number -= 1
#         if self.index == len(self.sequence):
#             self.index = 0
#         index = self.index
#         self.index += 1
#         return self.sequence[index]


class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.number == self.index:
            raise StopIteration

        index = self.index
        self.index += 1
        return self.sequence[index % len(self.sequence)]








result1 = sequence_repeat('abc', 5)
for item in result1:
    print(item, end ='')


# result2 = sequence_repeat("def", 5)
# for item in result2:
#     print(item, end='')
