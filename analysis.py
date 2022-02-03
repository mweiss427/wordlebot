from decimal import *
from operator import contains


class Words:
    list = []

    def __init__(self):
        self.list = []
        with open("words/common_words.txt", "r") as word_file:
            for text in word_file:
                self.list.append(Word(text.lower().strip(), "uuuuu"))

    # Here we want the highest ranked word.
    # We have a list of words.
    # we are going to loop through and compare them.
    def getHighestRanked(self, answer):
        word = Word("hello", "uuuuu")
        for cword in self.list:
            answer.compare(word, cword)
        return(word)

    def getList(self):
        for word in self.list:
            print(word)
        return self.list


class Word:
    name = []
    map = []
    rank = 0

    def __init__(self, word, map):
        self.name = str(word)
        self.map = map
        self.rank = self.getInitialRank()

    def __eq__(self, other):
        if (self.name == other.name and self.map == other.map):
            return True
        return

    def printWord(self):
        print("word: " + str(self.name))
        print("map : " + str(self.map))
        print("rank : " + str(self.rank))

    def setMap(self, map):
        self.map = map

    """ """

    def updateRank(self, wordList):
        # first lets loop and zero out the words we know not to be true
        # now lets times by 5 for a 'r' and 2 for a w

        # Loop through the letters of the played words.
        #
        for word in wordList:
            for letter in word.letters():
                if(letter.map == "n" and self.name.__contains__(letter.char)):
                    self.rank = 0
                if(letter.map == "w"):
                    if(self.name.__contains__(letter.char)):
                        self.rank = self.rank * 2
                    elif(True):  # TODO to fix this to make it 0 if the index of the word is in the wrong place
                        self.rank = 0
                if(letter.map == "r"):
                    if(self.name.__contains__(letter.char)):  # index of sorts
                        self.rank = self.rank * 5
                    else:
                        self.rank = 0

    """
    gets an array of letters.
    """

    def letters(self):
        letters = []
        i = 0
        for char in self.name:
            letter = Letter(char, self.map[i], i)
            letters.append(letter)
            i = i+1

        return(letters)

    def getInitialRank(self):
        total = 0
        for letter in str(self.name):
            try:
                total = total + Letters.letters[letter]
            except:
                # nothing
                a = 2

        return(total)

    def isChallengerHigherValue(self, challangeWord):
        if(challangeWord.rank >= self.rank):
            return True
        return False

    def matchIndex(self, cletter):
        # if letter is the same and in the same location it is a match
        if(self.name[cletter.index] == cletter.char):
            return True
        return(False)

    def display(self):
        return(self.letters)

    def getValue(char):
        return(Letters.letters[char])


class Letter:
    char = ""
    map = ""
    index = 6

    def __init__(self, word, map, index):
        self.char = str(word)
        self.map = map
        self.index = index


"""This is the stored results
answer is where the letters will go if they are right
letters are all of the letters with an associated rank

debate should we check to see if the known letters are ...
in the word vs just value them crazy high rank
solved by checking for 0. two birds. or one data point? 
"""


class Answer:
    answer = ["", "", "", "", ""]
    letters = []

    def __init__(self):
        letters = Letters()

    # comparing two words, using the data we have stored as needed
    # aWord is not getting check if it is valid.
    # This is A word basised, but most of the time A is the defender or carry over
    # They should win most of the time, so it is up to B to prove its valititty
    # retrun the winning word
    def compare(self, aWord, bWord):
        if self.isPossible(bWord):
            if(self.getRank() < self.bWord.getRank()):
                return(bWord)
        return aWord

    # Make sure the word is possible
    def isPossible(self, word):
        for letter in word.name:
            if self.letters[letter] == 0:
                return False
        return True

    # Get the rank of the word
    # this is the fun part
    # in the right spot is key
    # that should be a multplier by 1000
    # Word is an object that is used
    # now the other way.  if the letter is 0 it is false,
    # since we aren't yet trmming are list we need to account... noob
    # I'm going to avoid caring about the w's that should be done by ranking
    def getRank(self, word):
        total = 1
        # match the indexes of the two words will get the answer letter from the array
        index = 0
        for letter in word.name:
            if(self.answer[index] == letter):
                # correct letter correct spot. to the moon!
                total*100000
            if(self.isPossible()):
                # burn it down never getting used.
                total = 0


"""Letters is a key value pair letters to a rank. 
I started with the rank of the % of the words on the internet per wikipedia"""


class Letters:
    letters = dict()

    def __init__(self):
        getcontext().prec = 5
        # this is ugly and gross and I"m a noob back off
        self.letters["a"] = float(Decimal(8.2))
        self.letters["b"] = float(Decimal(1.5))
        self.letters["c"] = float(Decimal(2.8))
        self.letters["d"] = float(Decimal(4.3))
        self.letters["e"] = float(Decimal(13.00))
        self.letters["f"] = float(Decimal(2.2))
        self.letters["g"] = float(Decimal(2.00))
        self.letters["h"] = float(Decimal(6.1))
        self.letters["i"] = float(Decimal(7.00))
        self.letters["j"] = float(Decimal(.15))
        self.letters["k"] = float(Decimal(.77))
        self.letters["l"] = float(Decimal(4.0))
        self.letters["m"] = float(Decimal(2.5))
        self.letters["n"] = float(Decimal(6.7))
        self.letters["o"] = float(Decimal(7.5))
        self.letters["p"] = float(Decimal(1.9))
        self.letters["q"] = float(Decimal(0.095))
        self.letters["r"] = float(Decimal(6.0))
        self.letters["s"] = float(Decimal(6.3))
        self.letters["t"] = float(Decimal(9.1))
        self.letters["u"] = float(Decimal(2.8))
        self.letters["v"] = float(Decimal(.98))
        self.letters["w"] = float(Decimal(2.4))
        self.letters["x"] = float(Decimal(.15))
        self.letters["y"] = float(Decimal(2.0))
        self.letters["z"] = float(Decimal(.074))
