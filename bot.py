from analysis import Letters, Word, Words, Answer

"""
Bot is our trusty ol'e thinker
"""


class Bot:
    answer = Answer()

    def __init__(self):
        self.answer = Answer()

    # The algorthm to determe the first word... meep-morp
    # First we need a list of words.
    # I got them from https://github.com/hannahcode/word-guessing-game
    # Then we use rank. the highest ranked word is selected

    def getFirstWord(self):
        words = Words()
        return(words.getHighestRanked(self.answer))


"""gets the second word
 differnt algothrms based on the number of turn """


def getSecondWord(wordList):
    words = Words()

    for word in words.list:
        word.updateRank(wordList)
    myword = words.getHighestRanked()
    return(myword)


def getThirdWord(wordList):
    words = Words()

    for word in words.list:
        word.updateRank(wordList)
    myword = words.getHighestRanked()
    return(myword)


def getFourthWord(wordList):
    words = Words()

    for word in words.list:
        word.updateRank(wordList)
    myword = words.getHighestRanked()
    return(myword)


def getFifthWord(wordList):
    words = Words()

    for word in words.list:
        word.updateRank(wordList)
    myword = words.getHighestRanked()
    return(myword)


def getSixthWord(wordList):
    words = Words()

    for word in words.list:
        word.updateRank(wordList)
    myword = words.getHighestRanked()
    return(myword)
