import json
import operator
import string
import random
import nltk
from nltk.corpus import wordnet as wn
from nltk import pos_tag, word_tokenize

# loads the json into a table
with open('../Data/redaali.json') as f:
    data = json.load(f)

# for removing specified characters from each line
translator = str.maketrans('', '', '!?.')


prp = ""
nn = ""
vbz = ""
jj = ""
'''
while(True):
    rand = random.randint(0, len(data["messages"])-1)
    line = data["messages"][rand]["content"]
    line = line.translate(translator)
    line = word_tokenize(line)
    line = nltk.pos_tag(line)
    #print(line)
    for i in line:
        if (i[1] == "PRP$"):
            prp = i[1]
        elif (i[1] == "NN"):
            nn = i[1]
        elif (i[1] == "VBZ"):
            vbz = i[1]
        elif (i[1] == "JJ"):
            jj = i[1]

        if (prp != "" and nn != "" and vbz != "" and jj != ""):
            break

print(prp + " " + nn + " " + vbz + " " + jj)
'''
yeet = "Yeah lmao cause mom wanted older brother to leave"
yeet = word_tokenize(yeet)
yeet = nltk.pos_tag(yeet)
print(yeet)

yeet = "lol i get what u mean but its better when the guys older"
yeet = word_tokenize(yeet)
yeet = nltk.pos_tag(yeet)
print(yeet)
