import random as random

x = [random.random() for i in range(0,100)]


print max(x)

def findmax(x):

    currentMax = x[0]


    for item in x:


        if item > currentMax:
            currentMax = item

    return currentMax

print findmax(x)
