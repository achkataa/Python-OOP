import unittest

from lab.car_manager import Car


class CarTests(unittest.TestCase):
    make = "make"
    model = "530d"
    fuel_consumption = 10
    fuel_capacity = 100

    # def test_car_make_property_when_working(self):
    #     car = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)
    #     actual = car.make = self.make
    #     self.assertEqual("make", actual)


    def test_car_make_property_none_expect_exception(self):
        car = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)
        with self.assertRaises(Exception) as context:
            car.make = None

        self.assertEqual("Make cannot be null or empty!", str(context))