class Word(object):
    content = ""
    prevWord = ""
    prevPOS = ""
    nextWord = ""
    nextPOS = ""

    def __init__(self, content, prevWord, prevPOS, nextWord, nextPOS):
        self.content = content
        self.prevWord = prevWord
        self.prevPOS = prevPOS
        self.nextWord = nextWord
        self.nextPOS = nextPOS

    def debugPrint(self):
        print(self.content, self.prevWord, self.nextWord)

    def getContent(self):
        return self.content

    def getPrevWord(self):
        return self.prevWord

    def getPrevPOS(self):
        return self.prevPOS

    def getNextWord(self):
        return self.nextWord

    def getNextPOS(self):
        return self.nextPOS
