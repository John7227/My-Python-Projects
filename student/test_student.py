import unittest

from student.student import Student

class TestStudent(unittest.TestCase):
    def test_that_student_name_and_grade_level_displays(self): # add assertion here
        student = Student("Peterson", 11)

        self.assertEqual("Peterson", student.name)
        self.assertEqual(11, student.grade_level)

    def test_that_when_a_student_is_moved_up_by_one_grade_the_grade_level_increases(self):
        student = Student("Peterson", 11)

        self.assertEqual(12, student.promote())

    def test_that_a_student_cannot_be_promoted_pass_grade_12_else_it_throws_an_illegal_error(self):
        student = Student("Peterson", 11)
        self.assertEqual(12, student.promote())
        self.assertRaises(ValueError, student.promote)

    def test_that_I_take_a_score_and_It_returns_true_if_it_is_a_pass(self):
        student = Student("Peterson", 11)

        self.assertTrue(student.has_passed(90))

    def test_that_it_throws_exception_when_the_score_is_below_zero(self):
        student = Student("Peterson", 11)

        self.assertRaises(ValueError, student.has_passed, -5)

    def test_that_it_throws_exception_when_the_score_is_above_100(self):
        student = Student("Peterson", 11)

        self.assertRaises(ValueError, student.has_passed, 500)

    def test_that_I_update_the_name_and_It_changes(self):
        student = Student("Peterson", 11)

        self.assertEqual("Daniel", student.update_name("Daniel"))

    def test_that_it_throws_error_if_a_name_not_written_when_updating_the_name(self):
        student = Student("Peterson", 11)

        self.assertRaises(ValueError, student.update_name,"")

    def test_If_the_student_Is_In_the_final_grade_level(self):
        student = Student("Peterson", 11)

        student.promote()
        self.assertTrue(student.is_graduating())


if __name__ == '__main__':
    unittest.main()
