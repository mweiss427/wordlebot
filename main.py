from bot import Bot
from analysis import Letters, Word
from decimal import *

# Hello this is my first 'real' bot I'm creating.
# So lets begin.  This bot will solve wordle I'm hoping for an average
# solve of lower than 3.5 average

# lets get to solving waht is best first word?
# first lets setup our bot and say hello to the world
autobot = Bot()
print("Hello World")
# lets begin...
fword = autobot.getFirstWord()
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
