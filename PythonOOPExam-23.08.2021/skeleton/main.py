

from project.astronaut.biologist import Biologist
from project.space_station import SpaceStation

#
# class TestSpaceStation(TestCase):
#     def setUp(self):
#         self.space_station = SpaceStation()
#
#     def test_add_when_invalid(self):
#         with self.assertRaises(Exception) as ex:
#             self.space_station.add_astronaut("Gosho", "Tosho")
#         self.assertEqual("Astronaut type is not valid!", str(ex.exception))
#
#     def test_when_astr_already_in_the_list(self):
#         astr = Biologist("Gosho")
#         self.space_station.astronaut_repository.add(astr)
#         self.assertEqual(f"Gosho is already added.", self.space_station.add_astronaut("Biologist", "Gosho"))
#
#     def test_add_on_success(self):
#         astr = Biologist("Gosho")
#         self.assertEqual(f"Successfully added Biologist: Gosho.", self.space_station.add_astronaut("Biologist", "Gosho"))
#         self.assertEqual([astr], self.space_station.astronaut_repository.astronauts)
#
#
#
#
#
# if __name__ == '__main__':
#     main()

ss = SpaceStation()
ss.add_astronaut("Biologist", "Gosho")
ss.add_astronaut("Biologist", "Pesho")
ss.add_astronaut("Biologist", "Misho")
ss.add_planet("Mars", "igla, pruchka, seno, korona")
print(ss.send_on_mission("Mars"))
print(ss.report())

