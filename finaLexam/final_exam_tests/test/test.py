from project.team import Team
from unittest import TestCase, main


class TestTeam(TestCase):
    def setUp(self):
        self.team = Team("Levski")

    def test_attr_are_set(self):
        self.assertEqual("Levski", self.team.name)
        self.assertEqual({}, self.team.members)

    def test_name_property(self):
        with self.assertRaises(ValueError) as ex:
            self.team.name = "Levski4"
        self.assertEqual("Team Name can contain only letters!", str(ex.exception))

    def test_add_on_success(self):
        self.assertEqual("Successfully added: Gosho", self.team.add_member(Gosho=10))

    def test_add_when_there_is_already_that_name_in_the_list(self):
        self.team.members = {"Gosho": 10}
        self.team.add_member(Gosho=11)
        self.assertEqual({"Gosho": 10}, self.team.members)

    def test_remove_member_when_member_doesnt_exist(self):
        self.assertEqual(f"Member with name Gosho does not exist", self.team.remove_member("Gosho"))
        self.assertEqual({}, self.team.members)

    def test_remove_member_on_success(self):
        self.team.members = {"Gosho": 10}
        self.assertEqual(f"Member Gosho removed", self.team.remove_member("Gosho"))
        self.assertEqual({}, self.team.members)

    def test_gt(self):
        self.team.members = {"Gosho": 10}
        team2 = Team("CSKA")
        self.assertEqual(True, self.team.__gt__(team2))

    def test_gt_when_false(self):
        self.team.members = {"Gosho": 10}
        team2 = Team("CSKA")
        team2.members = {"Tosho": 15, "Misho": 10}
        self.assertEqual(False, self.team.__gt__(team2))


    def test_len(self):
        self.team.members = {"Gosho": 10}
        self.assertEqual(1, self.team.__len__())

    def test_add(self):
        team2 = Team("CSKA")
        self.team.members = {"Gosho": 10}
        team2.members = {"Tosho": 12}
        new_team = self.team.__add__(team2)
        self.assertEqual("LevskiCSKA", new_team.name)
        self.assertEqual({"Gosho": 10, "Tosho": 12}, new_team.members)

    def test_add_when_names_are_equal(self):
        team2 = Team("CSKA")
        self.team.members = {"Gosho": 10}
        team2.members = {"Gosho": 12}
        new_team = self.team.__add__(team2)
        self.assertEqual("LevskiCSKA", new_team.name)
        self.assertEqual({"Gosho": 10}, new_team.members)


    def test_str(self):
        self.team.add_member(Tosho=12)
        self.team.add_member(Misho=15)
        string = "Team name: Levski\nMember: Misho - 15-years old\nMember: Tosho - 12-years old"
        self.assertEqual(string, self.team.__str__())









if __name__ == '__main__':
    main()
