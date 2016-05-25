#import praw
import markovChain as MC

f = open('workfile.txt', 'rt')
# arraything = []
# for line in f:
#     arraything.append(line)
#
# for line in f:
#     tokens = nltk.word_tokenize(line)
#     print(tokens)


x = MC.TextMarkovChain(f)

x.RemoveFromChain("fucking jews")

# print(x.ProgressThroughChain())
