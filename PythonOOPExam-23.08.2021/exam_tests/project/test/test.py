from project.library import Library
from unittest import TestCase, main

class TestLibrary(TestCase):
    def setUp(self):
        self.library = Library("zdrave")

    def test_attrs_are_set(self):
        self.assertEqual("zdrave", self.library._Library__name)
        self.assertEqual("zdrave", self.library.name)
        self.assertEqual({}, self.library.readers)
        self.assertEqual({}, self.library.books_by_authors)

    def test_name_property_when_invalid_name_is_given(self):
        with self.assertRaises(ValueError) as ex:
            self.library.name = ''
        self.assertEqual("Name cannot be empty string!", str(ex.exception))

    def test_add_book_when_author_is_not_in_the_dict_and_book_is_not_in_the_dict(self):
        self.library.add_book("JK", "Harry")
        self.assertEqual({"JK": ["Harry"]}, self.library.books_by_authors)

    def test_add_reader_when_reader_is_not_in_the_dict(self):
        self.library.add_reader("Gosho")
        self.assertEqual({"Gosho": []}, self.library.readers)

    def test_add_reader_when_reader_is_already_there_should_return_message(self):
        self.library.readers = {"Gosho": []}
        self.assertEqual(f"Gosho is already registered in the zdrave library.", self.library.add_reader("Gosho"))

    def test_rent_book_when_reader_is_not_in_the_dict_should_return_a_message(self):
        self.assertEqual(f"Gosho is not registered in the zdrave Library.", self.library.rent_book("Gosho", "JK", "Harry"))

    def test_rent_book_when_author_is_not_in_the_dict_should_return_a_message(self):
        self.library.readers = {"Gosho": []}
        self.assertEqual(f"zdrave Library does not have any JK's books.", self.library.rent_book("Gosho", "JK", "Harry"))

    def test_rent_book_when_book_is_not_in_the_dict_should_return_a_message(self):
        self.library.readers = {"Gosho": []}
        self.library.books_by_authors = {"JK": []}
        self.assertEqual(f"""zdrave Library does not have JK's "Harry".""", self.library.rent_book("Gosho", "JK", "Harry"))

    def test_rent_book_when_success(self):
        self.library.readers = {"Gosho": []}
        self.library.books_by_authors = {"JK": ["Harry"]}
        self.library.rent_book("Gosho", "JK", "Harry")
        self.assertEqual({"Gosho": [{"JK": "Harry"}]}, self.library.readers)
        self.assertEqual({"JK": []}, self.library.books_by_authors)





if __name__ == '__main__':
    main()
