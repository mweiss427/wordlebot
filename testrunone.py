import unittest
from analysis import Letters, Word, Words, Letter
from bot import getNextWord


class TestStringMethods(unittest.TestCase):
    def testIsChallengerHigherValue(self):
        enter = Word("enter", "uuuuu")
        phone = Word("phone", "uuuuu")
        self.assertFalse(enter.isChallengerHigherValue(phone))


if __name__ == '__main__':
    unittest.main()
