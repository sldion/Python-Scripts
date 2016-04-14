import random as random

suits = ['heart','spades','clubs','diamonds']

ranks = range(1,14)

deck = {}
i = 0
for suit in  suits:
    for rank in ranks:
        deck[i] = [suit, rank]
        i = i +1

shuffleDeck = {}
x = range(0,52)
count = 0
while(any(deck)):

    y = x[ random.randint(0,len(x) - 1)]

    x.remove(y)

    shuffleDeck[count] = deck[y]
    deck.pop(y,None)
    count = count + 1


print shuffleDeck
