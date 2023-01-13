import unittest

from lab.extended_list import IntegerList


class ExtendedListTests(unittest.TestCase):
    def test_extended_list_add_int_should_add_it(self):
        integer_list = IntegerList(1, 2, 3, 4)
        internal_list = integer_list.add(5)
        expected = [1, 2, 3, 4, 5]
        self.assertEqual(expected, internal_list)

    def test_extended_list_add_string_should_return_exception(self):
        integer_list = IntegerList(1, 2, 3, 4)
        with self.assertRaises(ValueError):
            integer_list.add("t")

    def test_extended_list_remove_index_when_valid_should_remove_it(self):
        integer_list = IntegerList(1, 2, 3, 4)
        integer_list.remove_index(2)
        expected = [1, 2, 4]
        self.assertEqual(expected, integer_list.get_data())

    def test_extended_list_remove_index_when_negative_invalid_should_return_index_error(self):
        integer_list = IntegerList(1, 2, 3, 4)
        with self.assertRaises(IndexError):
            integer_list.remove_index(-5)

    def test_extended_list_remove_index_when_positive_invalid_should_return_index_error(self):
        integer_list = IntegerList(1, 2, 3, 4)
        with self.assertRaises(IndexError):
            integer_list.remove_index(4)

    def test_extended_list_init_when_not_only_integers_given_should_not_work(self):
        with self.assertRaises(Exception):
            IntegerList(1, 2, 3, 4, "str")

    def test_extended_list_init_when_only_integers_given_should_work(self):
        IntegerList(1, 2, 3, 4)

    def test_extended_list_get_when_valid_index_is_given_should_return_the_element(self):
        integer_list = IntegerList(1, 2, 3, 4)
        element_to_return = integer_list.get(2)
        self.assertEqual(3, element_to_return)

    def test_extended_list_get_when_negative_invalid_is_given_should_return_index_error(self):
        integer_list = IntegerList(1, 2, 3, 4)
        with self.assertRaises(IndexError):
            integer_list.get(-5)

    def test_extended_list_get_when_positive_invalid_is_given_should_return_index_error(self):
        integer_list = IntegerList(1, 2, 3, 4)
        with self.assertRaises(IndexError):
            integer_list.get(4)

    def test_extended_list_insert_when_valid_int_is_given_should_insert_it(self):
        integer_list = IntegerList(1, 2, 3, 4)
        integer_list.insert(0, 0)
        result = integer_list.get_data()
        expected = [0, 1, 2, 3, 4]
        self.assertEqual(expected, result)

    def test_extended_list_insert_when_positive_int_is_given_should_return_index_error(self):
        integer_list = IntegerList(1, 2, 3, 4)
        with self.assertRaises(IndexError):
            integer_list.insert(4, 0)

    def test_extended_list_insert_when_not_int_is_given_should_return_value_error(self):
        integer_list = IntegerList(1, 2, 3, 4)
        with self.assertRaises(ValueError):
            integer_list.insert(0, "gei")

    def test_get_biggest_should_work(self):
        integer_list = IntegerList(1, 2, 3, 4)
        actual = integer_list.get_biggest()
        expected = 4
        self.assertEqual(expected, actual)

    def test_get_index_should_work(self):
        integer_list = IntegerList(1, 2, 3, 4)
        expected = 2
        actual = integer_list.get_index(3)
        self.assertEqual(expected, actual)









