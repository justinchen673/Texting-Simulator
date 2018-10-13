import json
import operator
import string
import random
import nltk
from nltk.corpus import wordnet as wn

# loads the json into a table
with open('../Data/redaali.json') as f:
    data = json.load(f)

# for removing specified characters from each line
translator = str.maketrans('', '', '!?.')

while(True):
    rand = random.randint(0, len(data["messages"]))
    line = data["messages"][rand]["content"]
    line = line.translate(translator)
    line = line.split()
    
