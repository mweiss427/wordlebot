from analysis import Letters, Word, Words

"""
Bot is our trusty ol'e thinker it will make the human actions
"""


def __init__(self):
    a = 0


"""
The algorthm that gets the first word.
"""


def getFirstWord():
    words = Words()
    # words.getHighestRanked()
    word = Word("enter", 'uuuuu')
    return(word)


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
