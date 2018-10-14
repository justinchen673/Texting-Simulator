import json
import operator
import string
import nltk
import random
from nltk.corpus import wordnet as wn
from nltk import pos_tag, word_tokenize

def printRandPOS(data, pos):
    rand = random.randint(0, len(data[pos])-1)
    print(data[pos][rand])

#nltk.download('wordnet')
#nltk.download('punkt')
#nltk.download('averaged_perceptron_tagger')

# TODO: Get rid of hyperlinks, which are either https:// or http://
#       Punctuation still isn't removed? work on that, and symbols like < > : ;
#       Also try to account for punctuation in the text generator
#       "You missed a call from ______" shouldn't be a message
#       slang dictionary???
#       run through dictionary and find out what isn't defined
#       emojis & stickers or "like" button

# loads the json into a table
with open('../Data/redaali.json') as f:
    data = json.load(f)

# initialize variables
wordCount = 0
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
            for j in line:
                #if j[1].lower() in pos:
            #        pos[j[1].lower()].append(j[0])

                wordCount += 1
                modifiedWord = j[0] + ' ' + j[1]
                if modifiedWord.lower() in words:
                    words[modifiedWord.lower()] += 1
                else:
                    words[modifiedWord.lower()] = 1

# sorts the words by number of times it appears
sortedWords = sorted(words.items(), key=operator.itemgetter(1))

for x in sortedWords:
    print(x)
'''
print(len(data["messages"]), "messages")
print(wordCount, "words")
#print(pos)

printRandPOS(pos, "prp")
printRandPOS(pos, "vbp")
printRandPOS(pos, "nns")
print(pos["uh"])

#print(pos[""])
'''
'''
#nouns = {x.name().split('.', 1)[0] for x in wn.all_synsets('NN')}
#verbs = {x.name().split('.', 1)[0] for x in wn.all_synsets('v')}
#pronouns = {x.name().split('.', 1)[0] for x in wn.all_synsets('')}

asdf = "light" in nouns
print(asdf)


text = word_tokenize("My name is pewpepppepepepp")
text = nltk.pos_tag(text)
for i in text:
    print(i)
print(text)

#[('They', 'PRP'), ('refuse', 'VBP'), ('to', 'TO'), ('permit', 'VB'), ('us', 'PRP'),
#('to', 'TO'), ('obtain', 'VB'), ('the', 'DT'), ('refuse', 'NN'), ('permit', 'NN')]
'''
