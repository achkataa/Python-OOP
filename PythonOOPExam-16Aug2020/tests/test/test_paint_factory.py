from unittest import TestCase, main

from project.factory.paint_factory import PaintFactory


class TestPaintFactory(TestCase):
    def setUp(self):
        self.paint_factory = PaintFactory("Factory", 50)

    def test_attrs_are_set(self):
        self.paint_factory.valid_ingredients = ["white", "yellow"]
        self.paint_factory.ingredients = {"white": 10, "yellow": 10}
        self.assertEqual("Factory", self.paint_factory.name)
        self.assertEqual(50, self.paint_factory.capacity)
        self.paint_factory.valid_ingredients = ["white", "yellow"]
        self.assertEqual(["white", "yellow"], self.paint_factory.valid_ingredients)
        self.assertEqual({"white": 10, "yellow": 10}, self.paint_factory.ingredients)

    def test_add_ingredient_when_ingredient_not_in_list_should_raise_exception(self):
        self.paint_factory.valid_ingredients = ["white", "yellow"]
        with self.assertRaises(TypeError) as ex:
            self.paint_factory.add_ingredient("red", 10)

        self.assertEqual(f"Ingredient of type red not allowed in PaintFactory", str(ex.exception))

    def test_add_ingredient_when_no_capacity_in_the_factory_should_raise_exception(self):
        self.paint_factory.valid_ingredients = ["white", "yellow"]
        self.paint_factory.capacity = 10
        with self.assertRaises(ValueError) as ex:
            self.paint_factory.add_ingredient("white", 20)

        self.assertEqual("Not enough space in factory", str(ex.exception))

    def test_add_ingredient_success_should_add_ingredient_to_the_dict(self):
        self.paint_factory.valid_ingredients = ["white", "yellow"]
        self.paint_factory.ingredients = {}
        self.paint_factory.add_ingredient("white", 5)
        self.assertEqual({"white": 5}, self.paint_factory.ingredients)

    def test_remove_ingredient_when_there_is_not_such_ingredient_should_raise_exception(self):
        self.paint_factory.ingredients = {}
        with self.assertRaises(KeyError):
            self.paint_factory.remove_ingredient("white", 5)

    def test_remove_ingredient_when_there_is_not_capacity_left_should_raise_exception(self):
        self.paint_factory.ingredients = {"white": 10}
        with self.assertRaises(ValueError) as ex:
            self.paint_factory.remove_ingredient("white", 11)

        self.assertEqual("Ingredients quantity cannot be less than zero", str(ex.exception))

    def test_remove_ingredient_when_success_should_remove_the_given_quantity(self):
        self.paint_factory.ingredients = {"white": 10}
        self.paint_factory.remove_ingredient("white", 8)
        self.assertEqual({"white": 2}, self.paint_factory.ingredients)

    def test_property_should_return_ingredients(self):
        self.paint_factory.ingredients = {"white": 10}
        self.assertEqual({"white": 10}, self.paint_factory.products)


if __name__ == '__main__':
    main()

    