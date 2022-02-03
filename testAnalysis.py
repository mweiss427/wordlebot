from operator import le
import unittest
from analysis import Letters, Word, Words, Letter


class TestStringMethods(unittest.TestCase):

    ################## WORDS ##################

    ################## WORD ##################
    def test__eq__(self):
        enter = Word("enter", "uuuuu")
        phone = Word("phone", "uuuuu")
        self.assertFalse(enter == phone)

    def testUpdateRank(self):
        word = Word("enter", "nnwnn")
        phone = Word("phone", "nnwnn")
        wordList = [phone]
        self.assertTrue(word.rank > 0)
        word.updateRank(wordList)
        self.assertEqual(word.rank, 0)

    def testIsChallengerHigherValue(self):
        enter = Word("enter", "uuuuu")
        phone = Word("phone", "uuuuu")
        self.assertFalse(enter.isChallengerHigherValue(phone))

    def testLetters(self):
        enter = Word("enter", "nnwnn")
        letters = enter.letters()
        e = Letter('e', 'n', 0)
        self.assertEqual(letters[0].char, e.char)
        self.assertEqual(letters[0].map, e.map)
        self.assertEqual(letters[0].index, e.index)

    def testLetters(self):
        enter = Word("enter", "nnwnn")
        letters = enter.letters()
        r = Letter('r', 'n', 4)
        self.assertEqual(letters[4].char, r.char)
        self.assertEqual(letters[4].map, r.map)
        self.assertEqual(letters[4].index, r.index)

    def testsMatchIndex(self):
        enter = Word("enter", "uuuuu")
        letters = enter.letters()
        e = Letter('e', 'u', 0)
        self.assertTrue(enter.matchIndex(e))

    def testsMatchIndexFalse(self):
        enter = Word("enter", "uuuuu")
        letters = enter.letters()
        q = Letter('q', 'u', 0)
        self.assertFalse(enter.matchIndex(q))


if __name__ == '__main__':
    unittest.main()
