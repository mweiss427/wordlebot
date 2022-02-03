from operator import le
import unittest
from analysis import Letters, Word, Words, Letter


class TestStringMethods(unittest.TestCase):

    ################## WORDS ##################

    def testTrimList(self):
        words = Words()
        beforeWordCount = len(words.list)
        enter = Word("enter", "wnwnn")
        wordList = [enter]
        words.trimList(wordList)
        afterWordCount = len(words.list)
        self.assertTrue(151 > afterWordCount)

    def testRightLetter(self):
        words = Words()
        p = Letter("p", "n", 0)
        beforeWordCount = len(words.list)
        words.rightLetter(p)
        afterWordCount = len(words.list)
        self.assertTrue(beforeWordCount > afterWordCount)

    def testWrongLetter(self):
        words = Words()
        p = Letter("p", "n", 0)
        beforeWordCount = len(words.list)
        words.wrongLetter(p)
        afterWordCount = len(words.list)
        self.assertTrue(beforeWordCount > afterWordCount)

    def testWrongSpot(self):
        words = Words()
        letter = Letter("e", "w", 0)
        beforeCount = len(words.list)
        words.wrongSpot(letter)
        afterCount = len(words.list)
        self.assertTrue(beforeCount > afterCount)

    def testRemove(self):
        words = Words()
        enter = Word("enter", "uuuuu")
        naughty_list = [enter]
        words.remove(naughty_list)
        for word in words.list:
            self.assertTrue(enter.name != word.name)

    def testYeeshRemove(self):
        words = Words()
        yeesh = Word("yeesh", "uuuuu")
        naughty_list = [yeesh]
        words.remove(naughty_list)
        for word in words.list:
            self.assertTrue("yeesh" != word.name)

    ################## WORD ##################
    def test__eq__(self):
        enter = Word("enter", "uuuuu")
        phone = Word("phone", "uuuuu")
        self.assertFalse(enter == phone)

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
