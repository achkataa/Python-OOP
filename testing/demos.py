import unittest

def validate(value, types):
    if type(value) not in types:
        raise ValueError("Numbers should be only int and float type")


def my_sum(numbers):
    [validate(x, (int, float)) for x in numbers]
    return sum(numbers)


class SampleTest(unittest.TestCase):
    def test_equal(self):
        numbers = [1, 2, 3]
        actual_result = my_sum(numbers)
        expected_result = 6

        self.assertEqual(expected_result, actual_result)

    def test_when_strings_given(self):
        numbers = ["1", "2", "3"]
        with self.assertRaises(ValueError):
            my_sum(numbers)


    def test_when_numbers_are_float(self):
        numbers = [1.0, 2.0, 3.0]
        actual = my_sum(numbers)
        expected = 6.0
        self.assertEqual(expected, actual)


