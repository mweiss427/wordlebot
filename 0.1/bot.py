from analysis import Letters, Word, Words, Answer

"""
Bot is our trusty ol'e thinker
"""


class Bot:
    answer = Answer()
    words = Words()

    def __init__(self):
        self.answer = Answer()
        self.words = Words()

    # Autorunner - Devops day
    # We need ot make the tests be able to quickly setup testing.
    # See the details in testbot.py

    # Here is our first bot helper.
    # input a guess into the bot's knowledge
    def input(self, word):
        self.answer.updateAnswer(word)

    # The algorthm to determe the first word... meep-morp
    # First we need a list of words.
    # I got them from https://github.com/hannahcode/word-guessing-game
    # Then we use rank. the highest ranked word is selected

    def getFirstWord(self):
        return(self.words.getHighestRanked(self.answer))

    def getSecondWord(self):
        myword = self.words.getHighestRanked(self.answer)
        print(self.answer.answer)
        return(myword)

    def getThirdWord(self):
        myword = self.words.getHighestRanked(self.answer)
        print(self.answer.answer)
        return(myword)

    def getFourthWord(self, wordList):
        for word in wordList:
            self.answer.updateAnswer(word)
        myword = self.words.getHighestRanked(self.answer)
        print(self.answer.answer)
        return(myword)

    def getFifthWord(self, wordList):
        for word in wordList:
            self.answer.updateAnswer(word)
        myword = self.words.getHighestRanked(self.answer)
        print(self.answer.answer)
        return(myword)

    def getSixthWord(self, wordList):
        for word in wordList:
            self.answer.updateAnswer(word)
        myword = self.words.getHighestRanked(self.answer)
        print(self.answer.answer)
        return(myword)
