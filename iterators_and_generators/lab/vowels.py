### SOLUTION WITH ITERATORS

# class vowels:
#     VOWELS = ["A", "a", "E", "e", "O", "o", "U", "u", "I", "i", "Y", "y"]
#     def __init__(self, string):
#         self.string = string
#         self.index = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.index >= len(self.string):
#             raise StopIteration
#         ch = self.string[self.index]
#         self.index += 1
#         if not ch in vowels.VOWELS:
#             return self.__next__()
#         return ch

### SOLUTIN WITH GENERATOR FUNCTION

# def vowels(text):
#     vowel_letters = ["A", "a", "E", "e", "O", "o", "U", "u", "I", "i", "Y", "y"]
#     for char in text:
#         if char in vowel_letters:
#             yield char


### SOLUTIN WITH GENERATOR EXPRESSION (COMPREHENSION)
def vowels(text):
    vowel_letters = ["A", "a", "E", "e", "O", "o", "U", "u", "I", "i", "Y", "y"]
    return (ch for ch in text if ch in vowel_letters)





my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
