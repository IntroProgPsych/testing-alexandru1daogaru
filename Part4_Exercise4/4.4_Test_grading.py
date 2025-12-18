import unittest
from grading import grade_student


class TestGradeStudent(unittest.TestCase):
    def test_typical_values(self):
        self.assertEqual(grade_student(95), "A")
        self.assertEqual(grade_student(85), "B")
        self.assertEqual(grade_student(75), "C")
        self.assertEqual(grade_student(65), "D")
        self.assertEqual(grade_student(30), "F")

    def test_boundary_values(self):
        self.assertEqual(grade_student(90), "A")
        self.assertEqual(grade_student(89), "B")
        self.assertEqual(grade_student(80), "B")
        self.assertEqual(grade_student(79), "C")
        self.assertEqual(grade_student(70), "C")
        self.assertEqual(grade_student(69), "D")
        self.assertEqual(grade_student(60), "D")
        self.assertEqual(grade_student(59), "F")

    def test_invalid_scores(self):
        with self.assertRaises(ValueError):
            grade_student(-1)
        with self.assertRaises(ValueError):
            grade_student(101)


if __name__ == "__main__":
    unittest.main()
