from project.pet_shop import PetShop
from unittest import TestCase, main


class TestPetShop(TestCase):
    def setUp(self):
        self.pet_shop = PetShop("pupis")

    def test_attr_are_set(self):
        self.assertEqual("pupis", self.pet_shop.name)
        self.assertEqual({}, self.pet_shop.food)
        self.assertEqual([], self.pet_shop.pets)

    def test_add_food_when_quantity_is_less_than_0_should_raise_exception(self):
        with self.assertRaises(ValueError) as ex:
            self.pet_shop.add_food("gosho", 0)
        self.assertEqual('Quantity cannot be equal to or less than 0', str(ex.exception))

    def test_add_food_when_success(self):
        self.assertEqual("Successfully added 20.00 grams of gosho.", self.pet_shop.add_food("gosho", 20))
        self.assertEqual({"gosho":20}, self.pet_shop.food)

    def test_add_pet_when_there_is_such_a_pet_in_the_list(self):
        self.pet_shop.pets = ["gosho"]
        with self.assertRaises(Exception) as ex:
            self.pet_shop.add_pet("gosho")
        self.assertEqual("Cannot add a pet with the same name", str(ex.exception))

    def test_add_pet_when_success(self):
        self.pet_shop.pets = []
        self.assertEqual("Successfully added gosho.", self.pet_shop.add_pet("gosho"))
        self.assertEqual(["gosho"], self.pet_shop.pets)

    def test_feed_pet_when_there_is_not_such_pet_in_the_list_should_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.pet_shop.feed_pet("hrana", "Gosho")
        self.assertEqual("Please insert a valid pet name", str(ex.exception))

    def test_feed_pet_when_there_is_not_such_food_should_return_a_message(self):
        self.pet_shop.pets.append("Gosho")
        self.assertEqual("You do not have hrana", self.pet_shop.feed_pet("hrana", "Gosho"))

    def test_feed_pet_when_food_is_too_little(self):
        self.pet_shop.pets = ["Gosho"]
        self.pet_shop.food = {"granuli": 20}
        self.assertEqual("Adding food...", self.pet_shop.feed_pet("granuli", "Gosho"))
        self.assertEqual(1020,  self.pet_shop.food["granuli"])

    def test_feed_pet_on_success(self):
        self.pet_shop.pets = ["Gosho"]
        self.pet_shop.food = {"granuli": 100}
        self.assertEqual("Gosho was successfully fed", self.pet_shop.feed_pet("granuli", "Gosho"))
        self.assertEqual(0, self.pet_shop.food["granuli"])

    def test_repr(self):
        self.pet_shop.pets = ["Gosho", "Tosho"]
        self.assertEqual(f'Shop pupis:\nPets: Gosho, Tosho', repr(self.pet_shop))







if __name__ == '__main__':
    main()