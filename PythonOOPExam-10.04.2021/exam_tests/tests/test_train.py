from unittest import TestCase, main

from project.train.train import Train


class TestTrain(TestCase):
    def setUp(self):
        self.train = Train("Gosho", 3)

    def test_attr_are_set(self):
        self.assertEqual("Gosho", self.train.name)
        self.assertEqual(3, self.train.capacity)
        self.assertEqual([], self.train.passengers)

    def test_add_when_capacity_is_full_should_return_exception(self):
        self.train.passengers = ["Gosho", "Misho", "Tosho"]
        with self.assertRaises(ValueError) as ex:
            self.train.add("Gosho")
        self.assertEqual("Train is full", str(ex.exception))

    def test_add_when_passenger_already_in_the_list(self):
        self.train.passengers = ["Gosho"]
        with self.assertRaises(ValueError) as ex:
            self.train.add("Gosho")
        self.assertEqual("Passenger Gosho Exists", str(ex.exception))

    def test_add_on_success(self):
        self.train.passengers = []
        self.assertEqual("Added passenger Gosho", self.train.add("Gosho"))
        self.assertEqual(["Gosho"], self.train.passengers)

    def test_remove_when_there_is_not_such_a_passenger(self):
        self.train.passengers = []
        with self.assertRaises(ValueError) as ex:
            self.train.remove("Gosho")
        self.assertEqual("Passenger Not Found", str(ex.exception))

    def test_remove_when_success(self):
        self.train.passengers = ["Gosho"]
        self.assertEqual("Removed Gosho", self.train.remove("Gosho"))
        self.assertEqual([], self.train.passengers)


if __name__ == '__main__':
    main()