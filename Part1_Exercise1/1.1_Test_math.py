
import unittest
from mathexercise import add

class TestAddFunction(unittest.TestCase):
    # TODO:
    # - Write tests for:
    #   * adding two positive numbers
    #   * adding two negative numbers
    #   * adding a positive and a negative number
    # - Use assertEqual to check the results.
    # - Use clear method names, e.g. test_add_positive_numbers, etc.

    # write your tests here:
    def testfunction(self):
        self.assertEqual(add(2, 6)  ,8)
    
   


if __name__ == "__main__":
    unittest.main()
