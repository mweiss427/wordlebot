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
