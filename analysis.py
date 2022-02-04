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
        word = Word("zzzzz", "uuuuu")
        for cword in self.list:
            word = answer.compare(word, cword)
        return(word)

    def getList(self):
        for word in self.list:
            print(word)
        return self.list


class Word:
    name = []
    map = []
    rank = 1

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
    knownletters = []
    knownWrongDoubles = []

    def __init__(self):
        self.letters = Letters()
        self.knownletters = []

    # comparing two words, using the data we have stored as needed
    # aWord is not getting check if it is valid.
    # This is A word basised, but most of the time A is the defender or carry over
    # They should win most of the time, so it is up to B to prove its valititty
    # retrun the winning word
    def compare(self, aWord, bWord):
        if self.isPossible(bWord):
            if(self.getRank(aWord) < self.getRank(bWord)):
                return(bWord)
        return(aWord)

    # Make sure the word is possible
    def isPossible(self, word):
        # this checks to see if it isn't there at all.
        for letter in word.name:
            value = self.letters.letters[letter]
            if (value == 0):
                return False
            # I want to say, if it has a double letter.
            # and that letter is in the known wrong double list... it gone!
            if(word.name.count(letter) and self.knownWrongDoubles.__contains__(letter)):
                return False

        return True

    # Get the rank of the word
    # now the other way.  if the letter is 0 it is false,
    # in the right spot is key
    # that should be a multplier by 1000
    # Word is an object that is used
    # since we aren't yet trmming are list we need to account... noob
    def getRank(self, word):
        total = 1
        if(len(list(set(word.name))) == 5):
            total = 400
        if(len(list(set(word.name))) == 4):
            total = 30
        if(len(list(set(word.name))) == 3):
            total = 2
        if(len(list(set(word.name))) == 2):
            total = 1
        if(len(list(set(word.name))) == 1):
            total = 0

        # match the indexes of the two words will get the answer letter from the array
        index = 0
        if(not self.isPossible(word)):
            # burn it down never getting used.
            return 0
        for letter in word.name:
            total = total * self.letters.letters[letter]
            if(self.answer[index] == letter):
                # correct letter correct spot. to the moon!
                total*100000
            if(self.knownletters.__contains__(letter)):
                if(self.answer[index] == letter):
                    return 0  # Letter in wrong spot
                # To orbit
                total*1000
            index = index + 1
        word.rank = total
        return total

    # This should tweak the letters since that is where the ranking is truly held.
    def updateAnswer(self, playedWord):
        index = 0
        # first lets loop and zero out the letters we know not to be true
        for letter in playedWord.letters():
            if(letter.map == "n"):
                # we can't just do this due to double letter.
                if(self.answer.__contains__(letter.char)):
                    # something
                    # Sudo reseting the letter.  this needs a stat from online
                    # 2%... fuck it! Sure
                    self.letters.letters[letter.char] = 20
                    self.knownWrongDoubles.append(letter.char)
                else:
                    self.letters.letters[letter.char] = 0
            if(letter.map == "w"):
                self.knownletters.append(letter.char)
            if(letter.map == "r"):
                self.answer[index] = letter.char
            index = index + 1


"""Letters is a key value pair letters to a rank. 
I started with the rank of the % of the words on the internet per wikipedia"""


class Letters:
    letters = dict()

    def __init__(self):
        self.letters["a"] = 82
        self.letters["b"] = 15
        self.letters["c"] = 28
        self.letters["d"] = 43
        self.letters["e"] = 130
        self.letters["f"] = 22
        self.letters["g"] = 20
        self.letters["h"] = 61
        self.letters["i"] = 70
        self.letters["j"] = 2
        self.letters["k"] = 8
        self.letters["l"] = 4
        self.letters["m"] = 25
        self.letters["n"] = 67
        self.letters["o"] = 75
        self.letters["p"] = 19
        self.letters["q"] = 1
        self.letters["r"] = 60
        self.letters["s"] = 63
        self.letters["t"] = 91
        self.letters["u"] = 28
        self.letters["v"] = 9
        self.letters["w"] = 24
        self.letters["x"] = 2
        self.letters["y"] = 20
        self.letters["z"] = 1
