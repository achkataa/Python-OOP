from project.student_report_card import StudentReportCard
from unittest import TestCase, main

class TestStudentReportCard(TestCase):
    def setUp(self):
        self.student_report_card = StudentReportCard("Pesho", 7)

    def test_attrs_are_set(self):
        self.assertEqual("Pesho", self.student_report_card.student_name)
        self.assertEqual(7, self.student_report_card.school_year)
        self.student_report_card.grades_by_subject = {"Geography": [2, 4, 6]}
        self.assertEqual({"Geography": [2, 4, 6]}, self.student_report_card.grades_by_subject)

    def test_student_name_property_when_empty_string_is_given_should_return_exception(self):
        with self.assertRaises(ValueError) as ex:
            self.student_report_card.student_name = ""
        self.assertEqual("Student Name cannot be an empty string!", str(ex.exception))

    def test_school_year_when_number_under_2_is_given_should_return_exception(self):
        with self.assertRaises(ValueError) as ex:
            self.student_report_card.school_year = 0
        self.assertEqual("School Year must be between 1 and 12!", str(ex.exception))

    def test_school_year_when_number_over_12_is_given_should_return_exception(self):
        with self.assertRaises(ValueError) as ex:
            self.student_report_card.school_year = 13
        self.assertEqual("School Year must be between 1 and 12!", str(ex.exception))

    def test_add_grade_when_subject_is_already_in_dict_should_append_another_grade(self):
        self.student_report_card.grades_by_subject = {"Geography": [2, 4, 6]}
        self.student_report_card.add_grade("Geography", 5)
        self.assertEqual({"Geography": [2, 4, 6, 5]}, self.student_report_card.grades_by_subject)

    def test_add_grade_when_subject_is_not_in_the_dict_should_add_it_and_add_grade(self):
        self.student_report_card.grades_by_subject = {}
        self.student_report_card.add_grade("Geography", 5)
        self.assertEqual({"Geography": [5]}, self.student_report_card.grades_by_subject)

    def test_average_grade_by_subject_should_return_a_message(self):
        self.student_report_card.grades_by_subject = {"Geography": [5, 5]}
        self.assertEqual(f"Geography: {5:.2f}\n".strip(), self.student_report_card.average_grade_by_subject())

    def test_average_grade_for_all_subjects_should_return_message(self):
        self.student_report_card.grades_by_subject = {"Geography": [5, 5]}
        self.assertEqual(f"Average Grade: {5 :.2f}", self.student_report_card.average_grade_for_all_subjects())

    def test_repr(self):
        self.student_report_card.grades_by_subject = {"Geography": [5, 5]}
        expected = report = f"Name: Pesho\n" \
                 f"Year: 7\n" \
                 f"----------\n" \
                 f"Geography: {5:.2f}\n" \
                 f"----------\n" \
                 f"Average Grade: {5 :.2f}"
        actual = str(self.student_report_card)
        self.assertEqual(expected, actual)













if __name__ == '__main__':
    main()
