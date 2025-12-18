import unittest
from IsEven import is_even


class TestIsEven(unittest.TestCase):
    # TODO:
    # - Write tests for:
    #   * is_even(2) -> True
    #   * is_even(0) -> True
    #   * is_even(7) -> False
    #   * is_even(-4) -> True
    # - Use assertTrue / assertFalse to check the results.
    # - Use clear method names, e.g. test_even_positive_number, etc.
    #
    # write your tests here:

    def testtrueorfalse(self):
        self.assertTrue(is_even(6))
        self.assertFalse(is_even(1))


   


if __name__ == "__main__":
    unittest.main()

