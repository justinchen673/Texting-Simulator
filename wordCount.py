import json
import operator
import string

# TODO: Get rid of hyperlinks, which are either https:// or http://
#       Punctuation still isn't removed? work on that, and symbols like < > : ;
#       Also try to account for punctuation in the text generator
#       "You missed a call from ______" shouldn't be a message
#       slang dictionary???
#       run through dictionary and find out what isn't defined
#       emojis & stickers or "like" button



# loads the json into a table
with open('../Data/mcchickens.json') as f:
    data = json.load(f)

# initialize variables
wordCount = 0
words =	{
  "the": 0
}

# for removing specified characters from each line
translator = str.maketrans('', '', '!?.')
# loop through all messages
for i in range(0, len(data["messages"])):
    # obtain the message
    if ("content" in data["messages"][i]):
        line = data["messages"][i]["content"]
        line = line.translate(translator)
        # removes "x sent a photo", additional clause is for separating senders
        # and data["messages"][i]["sender_name"] == "name"
        if (line[-12:] != "sent a photo" and line[:8] != "https://"):
            # gets rid of whitespace
            line = data["messages"][i]["content"].split()
            # adds word to the hashtable if it doesn't exist
            for j in line:
                wordCount += 1
                if j.lower() in words:
                    words[j.lower()] += 1
                else:
                    words[j.lower()] = 1

# sorts the words by number of times it appears
sortedWords = sorted(words.items(), key=operator.itemgetter(1))

for x in sortedWords:
    print(x)

print(len(data["messages"]), "messages")
print(wordCount, "words")

