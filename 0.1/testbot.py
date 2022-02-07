import unittest
from analysis import Letters, Word, Words
from bot import Bot

# So the goal is 3.5 average try. so we will make sure the word
# will be solved within 3 attempts.  We can bank days as long as we get the word.
# this will keep history and maintain a good status.


class Test262022(unittest.TestCase):

    ############# Bot #############
    # Test for 2/6/2022
    # Word: skill
    def testGetFristWord(self):
        bot = Bot()
        self.assertEqual(bot.getFirstWord().name, Word("oaten", "uuuuu").name)

    def testGetSecondWord(self):
        bot = Bot()
        word = Word("oaten", "nnnnn")
        bot.input(word)
        self.assertEqual(bot.getSecondWord().name, Word("shiur", "uuuuu").name)

    def testGetThirdWord(self):
        bot = Bot()
        word = Word("oaten", "nnnnn")
        word = Word("shiur", "rnrnn")
        bot.input(word)
        word = bot.getThirdWord()
        print(word.name)
        self.assertEqual(bot.getThirdWord().name, Word("skill", "uuuuu").name)


if __name__ == '__main__':
    unittest.main()
