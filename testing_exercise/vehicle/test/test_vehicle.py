from unittest import TestCase, main

from project.vehicle import Vehicle


class TestVehicle(TestCase):
    def setUp(self):
        self.vehicle = Vehicle(50, 200)

    def test_attrs_are_set(self):
        self.assertEqual(50, self.vehicle.fuel)
        self.assertEqual(200, self.vehicle.horse_power)
        self.assertEqual(50, self.vehicle.capacity)
        self.assertEqual(1.25, Vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_drive_when_fuel_is_not_enough_should_return_exception(self):
        kilometers = 100
        fuel_needed = kilometers * 1.25
        with self.assertRaises(Exception) as context:
            self.vehicle.drive(kilometers)

        self.assertEqual("Not enough fuel", str(context.exception))

    def test_drive_when_fuel_is_enough_expect_to_decrease_the_fuel(self):
        kilometers = 5
        fuel_needed = kilometers * 1.25
        self.vehicle.drive(kilometers)
        self.assertEqual(43.75, self.vehicle.fuel)

    def test_refuel_when_too_much_fuel_is_given_expect_exception(self):
        new_fuel = 50
        with self.assertRaises(Exception) as context:
            self.vehicle.refuel(new_fuel)

        self.assertEqual("Too much fuel", str(context.exception))

    def test_refuel_when_enough_fuel_is_given_should_increase_the_fuel(self):
        new_fuel = 1
        self.vehicle.drive(5)
        self.vehicle.refuel(new_fuel)
        self.assertEqual(44.75, self.vehicle.fuel)

    def test_string_representation_should_return_a_message(self):
        result = str(self.vehicle)
        self.assertEqual(f"The vehicle has 200 horse power with 50 fuel left and 1.25 fuel consumption", result)














if __name__ == '__main__':
    main()