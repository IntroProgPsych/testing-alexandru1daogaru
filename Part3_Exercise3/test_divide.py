import unittest
from divide import safe_divide


class TestSafeDivide(unittest.TestCase):
    def test_division_integers(self):
        self.assertEqual(safe_divide(10, 2), 5.0)

    def test_division_floats(self):
        self.assertAlmostEqual(safe_divide(0.5, 0.1), 5.0)

    def test_division_by_zero(self):
        with self.assertRaises(ValueError) as cm:
            safe_divide(5, 0)
        self.assertEqual(str(cm.exception), "Division by zero is not allowed")


if __name__ == "__main__":
    unittest.main()
