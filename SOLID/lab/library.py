class Library:
    def __init__(self, books):
        self.books = books

    @property
    def books(self):
        return self.__books

    @books.setter
    def books(self, value):
        self.__books = value




class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


class Formatter:
    def format(self, book: Book):
        pass


class FormatToReturn(Formatter):
    def format(self, book: Book):
        return f"{book.title} added to the library"


class FormatToAddToLibrary(Formatter):
    def format(self, book: Book):
        return book.title




class AddBook:
    def add_book(self, book: Book, formatter: Formatter, library: Library):
        library.books.append(formatter.format(book))
        return formatter.format(book)

class SellBook:
    def sell_book(self, book: Book, formatter: Formatter, library: Library):
        if book in library.books:
            library.books.remove(book)
            return formatter.format(book)


library = Library(["Mecho Puh", "Robin hood", "The 5-second rule"])
book1 = Book("Rich dad poor dad", "robert keyosaki")
print(library.books)
AddBook().add_book(book1, Formatter(), library)
print(library.books)


