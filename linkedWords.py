import json
import operator
import string
import nltk
import random
from word import Word
from nltk.corpus import wordnet as wn
from nltk import pos_tag, word_tokenize


def printRandPOS(data, pos):
    rand = random.randint(0, len(data[pos])-1)
    randWord = data[pos][rand]
    randWord.debugPrint()

def printRandPOSBasedOnPrev(data, pos, prev, next):
    '''
    printed = False
    for i in range(0, len(data[pos]) - 1):
        randWord = data[pos][i]
        print(prev, randWord.getPrevPOS())
        if (prev == randWord.getPrevPOS()):
            print(randWord.getContent())
            printed = True
            break
    if (printed == False):
        print("No word matches :(")
    '''
    while (True):
        rand = random.randint(0, len(data[pos])-1)
        randWord = data[pos][rand]
        #print(prev, randWord.getPrevPOS(), next, randWord.getNextPOS())
        if (prev == randWord.getPrevPOS() and next == randWord.getNextPOS()):
            print(randWord.getContent())
            break





# loads the json into a table
with open('../Data/redaali.json') as f:
    data = json.load(f)

words =	{
    "the": 0
}
pos = {
    "cc": [],
    "cd": [],
    "dt": [],
    "ex": [],
    "in": [],
    "jj": [],
    "jjr": [],
    "jjs": [],
    "ls": [],
    "md": [],
    "nn": [],
    "nnp": [],
    "nns": [],
    "pdt": [],
    "prp": [],
    "prp$": [],
    "rb": [],
    "rbr": [],
    "rbs": [],
    "rp": [],
    "to": [],
    "uh": [],
    "vb": [],
    "vbd": [],
    "vbg": [],
    "vbn": [],
    "vbp": [],
    "vbz": [],
    "wdt": [],
    "wp": [],
    "wrb": []
}



# for removing specified characters from each line
translator = str.maketrans('', '', '!?,.\'')
# loop through all messages
for i in range(0, len(data["messages"])):
    # obtain the message
    if ("content" in data["messages"][i]):
        line = data["messages"][i]["content"]
        line = line.translate(translator)
        # removes "x sent a photo", additional clause is for separating senders
        # and data["messages"][i]["sender_name"] == "name"
        if (line[-12:] != "sent a photo" and line[:8] != "https://" and data["messages"][i]["sender_name"] == "Reda Ali"):
            line = word_tokenize(line)
            line = nltk.pos_tag(line)
            # adds word to the hashtable if it doesn't exist
            for j in range(0, len(line) - 1):
                if (line[j][1].lower() in pos):
                    if (j+1 >= len(line)):
                        nextWord = ""
                        nextPOS = ""
                    else:
                        nextWord = line[j+1][0]
                        nextPOS = line[j+1][1].lower()

                    if (j-1 < 0):
                        prevWord = ""
                        prevPOS = ""
                    else:
                        prevWord = line[j-1][0]
                        prevPOS = line[j-1][1].lower()

                    newWord = Word(line[j][0], prevWord, prevPOS, nextWord, nextPOS)
                    pos[line[j][1].lower()].append(newWord)
                #pos[j[1].lower()].append(j[0])
                '''
                wordCount += 1
                modifiedWord = j[0] + ' ' + j[1]
                if modifiedWord.lower() in words:
                    words[modifiedWord.lower()] += 1
                else:
                    words[modifiedWord.lower()] = 1
                    '''

'''
printRandPOSBasedOnPrevAndNext(pos, "prp", "", "")
printRandPOSBasedOnPrevAndNext(pos, "vbp", "prp", "")
printRandPOSBasedOnPrevAndNext(pos, "nns", "vbp", "")

printRandPOSBasedOnPrevAndNext(pos, "vbn", "", "in")
printRandPOSBasedOnPrevAndNext(pos, "in", "vbn", "prp")
printRandPOSBasedOnPrevAndNext(pos, "prp", "in", "")
printRandPOSBasedOnPrevAndNext(pos, "vbp", "prp", "")
printRandPOSBasedOnPrevAndNext(pos, "dt", "vbp", "")
printRandPOSBasedOnPrevAndNext(pos, "nn", "dt", "")

line = "come inside we have a table"
line = word_tokenize(line)
line = nltk.pos_tag(line)
print(line)
'''

rand2 = 0
while (True):
    rand2 = random.randint(0, len(data["messages"])-1)
    if (data["messages"][rand2]["sender_name"] == "Reda Ali"):
        break

line = data["messages"][rand2]["content"]
line = line.translate(translator)
line = word_tokenize(line)
line = nltk.pos_tag(line)
print(line)
for i in range(0, len(line)):
    if (i == 0):
        printRandPOSBasedOnPrev(pos, line[i][1].lower(), "", line[i+1][1].lower())
    elif (i == len(line) - 1):
        printRandPOSBasedOnPrev(pos, line[i][1].lower(), line[i-1][1].lower(), "")
    else:
        printRandPOSBasedOnPrev(pos, line[i][1].lower(), line[i-1][1].lower(), line[i+1][1].lower())
