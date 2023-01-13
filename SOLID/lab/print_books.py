from abc import ABC, abstractmethod
class Book:
    def __init__(self, name, content: str):
        self.name = name
        self.content = content


class Formatter(ABC):
    @abstractmethod
    def format(self, book: Book):
        pass


class FormatOnlyTheName(Formatter):
   def format(self, book: Book):
       return book.name

class FormatNameAndContent(Formatter):
   def format(self, book: Book):
       return f"{book.name} --- {book.content}"


class Printer:
    def get_book(self, book: Book, formatter: Formatter):
         return formatter.format(book)

book = Book("Rich Dad Poor Dad", "How to be financially free")
print(Printer().get_book(book, FormatOnlyTheName()))



