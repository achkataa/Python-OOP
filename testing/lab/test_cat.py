import unittest

from lab.cat import Cat


class TestCat(unittest.TestCase):
    name = "Macka"
    def setUp(self):
        self.cat = Cat(self.name)

    def test_cat_eat_size_should_be_increased(self):
        ### Cat's size is increased after eating ###
        self.cat.eat()
        self.assertEqual(1, self.cat.size)

    def test_cat_eat_fed_should_be_true(self):
        ### Cat is fed after eating ###
        self.cat.eat()
        self.assertTrue(self.cat.fed)
        pass

    def test_cat_eat_should_trow_exception_if_fed_true(self):
        ### Cat cannot eat if already fed, raises an error ###
        self.cat.eat()
        with self.assertRaises(Exception):
            self.cat.eat()

    def test_cat_sleep_when_cat_not_fed(self):
        ### Cat cannot fall asleep if not fed, raises an error ###
        with self.assertRaises(Exception):
            self.cat.sleep()

    def test_cat_is_not_sleepy_when_ate_after_sleep(self):
        ### Cat is not sleepy after sleeping ###
        self.cat.eat()
        self.cat.sleep()
        self.assertFalse(self.cat.sleepy)






