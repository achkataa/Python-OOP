# class dictionary_iter:
#     def __init__(self, dictionary):
#         self.dictionary = dictionary
#         self.counter = 0
#         self.keys = list(self.dictionary.keys())
#         self.values = list(self.dictionary.values())
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.counter == len(self.dictionary):
#             raise StopIteration
#
#         counter = self.counter
#         self.counter += 1
#         return (self.keys[counter], self.values[counter])
#



class dictionary_iter:
    def __init__(self, dictionary):
        self.dictionary = dictionary
        self.counter = 0

    def __iter__(self):
        return iter(self.dictionary.items())

    def __next__(self):
        return next(self.dictionary)
        # if self.counter == len(self.dictionary):
        #     raise StopIteration


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)

### SECOND SOLUTION (NOT FOR JUDGE)

# class dictionary_iter:
#     def __init__(self, dictionary):
#         self.dictionary = dictionary
#
#     def __iter__(self):
#         return iter([(key, value) for key, value in self.dictionary.items()])


#
# b = {1: "1", 2: "2"}
#
# print(list(b.keys()))
# print(list(b.values()))

