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

    # The algorthm to determe the first word... meep-morp
    # First we need a list of words.
    # I got them from https://github.com/hannahcode/word-guessing-game
    # Then we use rank. the highest ranked word is selected

    def getFirstWord(self):
        return(self.words.getHighestRanked(self.answer))

    def getSecondWord(self, wordList):
        for word in wordList:
            self.answer.updateAnswer(word)
        myword = self.words.getHighestRanked(self.answer)
        return(myword)

    def getThirdWord(self, wordList):
        for word in wordList:
            self.answer.updateAnswer(word)
        myword = self.words.getHighestRanked(self.answer)
        return(myword)

    def getFourthWord(self, wordList):
        for word in wordList:
            self.answer.updateAnswer(word)
        myword = self.words.getHighestRanked(self.answer)
        return(myword)

    def getFifthWord(self, wordList):
        for word in wordList:
            self.answer.updateAnswer(word)
        myword = self.words.getHighestRanked(self.answer)
        return(myword)

    def getSixthWord(self, wordList):
        for word in wordList:
            self.answer.updateAnswer(word)
        myword = self.words.getHighestRanked(self.answer)
        return(myword)
