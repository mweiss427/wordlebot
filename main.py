from bot import getFirstWord, getSecondWord, getThirdWord, getFourthWord, getFifthWord, getSixthWord
from analysis import Letters, Word
from decimal import *

print("Hello World")
fword = getFirstWord()
print(fword.printWord())
# r right place
# w wrong spot
# n nothing
# u unknown
print('''Enter String Map
# r right place
# w wrong spot
# n nothing''')
fword.setMap(input())

# Lets go get the next word
wordList = [fword]
fword.printWord()

sword = getSecondWord(wordList)
sword.printWord()
wordList.append(sword)

print('''Enter String Map
# r right place
# w wrong spot
# n nothing''')
sword.setMap(input())

tword = getThirdWord(wordList)
tword.printWord()
wordList.append(tword)

print('''Enter String Map
# r right place
# w wrong spot
# n nothing''')
tword.setMap(input())

fword = getFourthWord(wordList)
fword.printWord()
wordList.append(fword)
print('''Enter String Map
# r right place
# w wrong spot
# n nothing''')
fword.setMap(input())

fiveword = getFifthWord(wordList)
fiveword.printWord()
wordList.append(fiveword)

print('''Enter String Map
# r right place
# w wrong spot
# n nothing''')
fiveword.setMap(input())

sixword = getSixthWord(wordList)
sixword.printWord()
wordList.append(sixword)

print('''Enter String Map
# r right place
# w wrong spot
# n nothing''')
sixword.setMap(input())
