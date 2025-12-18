import unittest
from quizz import interpret_score

class TestQuizz(unittest.TestCase):

    def testInterpretScore(self):
        self.assertEqual(interpret_score(2), "Passed")


    if __name__=="__main__":
        unittest.main()
        