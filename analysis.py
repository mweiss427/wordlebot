from decimal import *
from operator import contains


class Words:
    list = []

    def __init__(self):
        self.list = []
        with open("words/common_words.txt", "r") as word_file:
            for text in word_file:
                self.list.append(Word(text.lower().strip(), "uuuuu"))

    def getList(self):
        for word in self.list:
            print(word)
        return self.list


class Word:
    name = []
    map = []

    def __init__(self, word, map):
        self.name = str(word)
        self.map = map

    def __eq__(self, other):
        if (self.name == other.name and self.map == other.map):
            return True
        return

    def printWord(self):
        print("word: " + str(self.name))
        print("map : " + str(self.map))

    def setMap(self, map):
        self.map = map

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

    def getValue(self):
        total = 0
        for letter in str(self.name):
            try:
                total = total + Letters.letters[letter]
            except:
                # nothing
                a = 2

        return(total)

    def isChallengerHigherValue(self, challangeWord):
        if(float(challangeWord.getValue()) >= float(self.getValue())):
            return True
        return False

    def matchIndex(self, cletter):
        # if letter is the same and in the same location it is a match
        if(self.name[cletter.index] == cletter.char):
            return True
        return(False)


class Letters:
    letters = dict()
    getcontext().prec = 5
    letters["a"] = float(Decimal(8.2))
    letters["b"] = float(Decimal(1.5))
    letters["c"] = float(Decimal(2.8))
    letters["d"] = float(Decimal(4.3))
    letters["e"] = float(Decimal(13.00))
    letters["f"] = float(Decimal(2.2))
    letters["g"] = float(Decimal(2.00))
    letters["h"] = float(Decimal(6.1))
    letters["i"] = float(Decimal(7.00))
    letters["j"] = float(Decimal(.15))
    letters["k"] = float(Decimal(.77))
    letters["l"] = float(Decimal(4.0))
    letters["m"] = float(Decimal(2.5))
    letters["n"] = float(Decimal(6.7))
    letters["o"] = float(Decimal(7.5))
    letters["p"] = float(Decimal(1.9))
    letters["q"] = float(Decimal(0.095))
    letters["r"] = float(Decimal(6.0))
    letters["s"] = float(Decimal(6.3))
    letters["t"] = float(Decimal(9.1))
    letters["u"] = float(Decimal(2.8))
    letters["v"] = float(Decimal(.98))
    letters["w"] = float(Decimal(2.4))
    letters["x"] = float(Decimal(.15))
    letters["y"] = float(Decimal(2.0))
    letters["z"] = float(Decimal(.074))
    letters["A"] = float(Decimal(8.2))
    letters["B"] = float(Decimal(1.5))
    letters["C"] = float(Decimal(2.8))
    letters["D"] = float(Decimal(4.3))
    letters["E"] = float(Decimal(13.00))
    letters["F"] = float(Decimal(2.2))
    letters["G"] = float(Decimal(2.00))
    letters["H"] = float(Decimal(6.1))
    letters["I"] = float(Decimal(7.00))
    letters["J"] = float(Decimal(.15))
    letters["K"] = float(Decimal(.77))
    letters["L"] = float(Decimal(4.0))
    letters["M"] = float(Decimal(2.5))
    letters["N"] = float(Decimal(6.7))
    letters["O"] = float(Decimal(7.5))
    letters["P"] = float(Decimal(1.9))
    letters["Q"] = float(Decimal(0.095))
    letters["R"] = float(Decimal(6.0))
    letters["S"] = float(Decimal(6.3))
    letters["T"] = float(Decimal(9.1))
    letters["U"] = float(Decimal(2.8))
    letters["V"] = float(Decimal(.98))
    letters["W"] = float(Decimal(2.4))
    letters["X"] = float(Decimal(.15))
    letters["Y"] = float(Decimal(2.0))
    letters["Z"] = float(Decimal(.074))

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
