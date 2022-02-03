import unittest
from analysis import Letters, Word, Words
from bot import getFirstWord, getNextWord


class TestStringMethods(unittest.TestCase):

    ############# Bot #############

    def testGetFristWord(self):
        self.assertEqual(getFirstWord().name, Word("enter", "uuuuu").name)

    def testGetFristWordMap(self):
        self.assertEqual(getFirstWord().map, Word("enter", "uuuuu").map)

    def testGetNextWordName(self):
        word = Word("enter", "wnwnn")
        list = [word]
        self.assertEqual(getNextWord(list).name, Word("steel", "uuuuu").name)

    def testGetNextWordMap(self):
        word = Word("enter", "nnwnn")
        list = [word]
        self.assertEqual(getNextWord(list).name, Word("hello", "uuuuu").name)


if __name__ == '__main__':
    unittest.main()
