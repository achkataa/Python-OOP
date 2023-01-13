import unittest
from lab.worker import Worker


class WorkerTests(unittest.TestCase):
    name = "Pesho"
    salary = 1000
    energy = 3

    def setUp(self):
        self.worker = Worker(self.name, self.salary, self.energy)


    def test_worker_init_correct_initialized_name_salary_energy(self):
        self.assertEqual(self.name, self.worker.name)
        self.assertEqual(self.salary, self.worker.salary)
        self.assertEqual(self.energy, self.worker.energy)

    def test_worker_when_rest_is_called_expect_energy_to_be_incremented(self):
        self.worker.rest()
        self.assertEqual(self.energy + 1, self.worker.energy)

    def test_worker_work_with_negative_power_should_raise_error(self):
        self.worker.energy = 0
        self.worker.work()
        with self.assertRaises(Exception):
            self.worker.work()

    def test_worker_work_increase_money_by_salary(self):
        self.worker.work()
        self.assertEqual(self.worker.salary, self.worker.money)

    def test_worker_work_energy_should_be_decreased(self):
        self.worker.work()
        self.assertEqual(self.energy - 1, self.worker.energy)

    def test_worker_get_info_should_return_correct_string(self):
        expected = f'{self.name} has saved 0 money.'
        actual = self.worker.get_info()
        self.assertEqual(expected, actual)