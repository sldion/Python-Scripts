
import random
import sys
"""Creates a MarkovChain out of a text file.
with some added functionality to parse the resulting dictionary

    addToChain: adds a list of strings to the markov chain

"""
class TextMarkovChain:
    MarkovChain = {}
    punctuation = ['.', '?', ',', '!', ';']
    NumberOfWords = 2

    def __init__(self, f, numberOfWords=2, removePunctuation=True):

        self.addToChain(f, removePunctuation=removePunctuation)
        self.NumberOfWords = numberOfWords

    def addToChain(self, f, removePunctuation=True):

        for line in f:
            wordLine = line.split()
            if removePunctuation:
                for word in wordLine:
                    if word[-1] in self.punctuation:
                        wordLine[wordLine.index(word)] = word[:-1]
                for i in range(0, len(wordLine) - self.NumberOfWords):
                    textKey = wordLine[i:i + self.NumberOfWords]
                    textKey = ' '.join(textKey)
                    if self.MarkovChain.get(textKey) is not None:
                        self.MarkovChain[textKey].append(
                                         wordLine[i + self.NumberOfWords])
                    else:
                        self.MarkovChain[textKey] = [wordLine[i + 2]]

            else:
                for i in range(0, len(wordLine) - self.NumberOfWords):
                    textKey = wordLine[i:i + self.NumberOfWords]
                    textKey = ' '.join(textKey)
                    if self.MarkovChain.get(textKey) is not None:
                        self.MarkovChain[textKey].append(
                                         wordLine[i + self.NumberOfWords])
                    else:
                        self.MarkovChain[textKey] = [wordLine[i + 2]]

    def get_chain(self):

        return self.MarkovChain

    def get_keys(self):

        return self.MarkovChain.keys()

    def addToPunctuation(self, character):
        self.punctuation.append(character)

    def ProgressThroughChain(self, startingPhrase=None):

        if startingPhrase is None:
            keys = list(self.MarkovChain.keys())
            chain = keys[random.randint(0, len(keys) - 1)]

            while self.MarkovChain.get(
                    ' '.join(chain.split()[-2:])) is not None:
                    newKey = ' '.join(chain.split()[-2:])

                    if len(self.MarkovChain[newKey]) - 1 == 0:
                        chain += ' ' + self.MarkovChain[newKey][0]

                    else:
                        chain += ' ' + self.MarkovChain[newKey][
                          random.randint(0, len(self.MarkovChain[newKey]) - 1)]

        return chain

    def RemoveFromChain(self, key):
        if self.MarkovChain.get(key) is not None:

            del self.MarkovChain[key]
        else:
            sys.stderr.write("error: %s\n" % "Key does not exist")
            sys.exit(1)
