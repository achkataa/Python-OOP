from unittest import TestCase, main

from project.mammal import Mammal


class TestMammal(TestCase):
    def setUp(self):
        self.mammal = Mammal("Peter", "type1", "mammal_sound")

    def test_if_attrs_are_set(self):
        self.assertEqual("Peter", self.mammal.name)
        self.assertEqual("type1", self.mammal.type)
        self.assertEqual("mammal_sound", self.mammal.sound)
        self.assertEqual("animals", self.mammal.get_kingdom())

    def test_make_sound_should_return_message(self):
        result = self.mammal.make_sound()
        self.assertEqual("Peter makes mammal_sound", result)

    def test_get_kingdom_should_return__kingdom(self):
        result = self.mammal.get_kingdom()
        self.assertEqual("animals", result)

    def test_info_should_return_message(self):
        result = self.mammal.info()
        self.assertEqual("Peter is of type type1", result)


if __name__ == '__main__':
    main()