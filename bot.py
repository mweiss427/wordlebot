from analysis import Letters, Word, Words


def __init__(self):
    a = 0


def getFirstWord():
    words = Words()
    # genesis word
    word = Word("zzzzz", "uuuuu")
    for cword in words.list:
        if word.isChallengerHigherValue(cword):
            word = cword
    return(word)


"""gets the next most likley word"""


def getNextWord(wordList):
    words = Words()

    for word in words:
        word.updateRank(wordList)

    return(word)
