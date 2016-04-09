import numpy as np
import csv as csv

# matches 6.86
with open('Matches.csv', 'rt') as csvfile:
    Data = csv.reader(csvfile, delimiter=',')
    next(Data)
    firstLine = True
    Sum = 0.0
    count = 0

    for row  in Data:
            Sum = Sum + float(row[8])
            count = count + 1
    print(Sum/count)
#matches 6.85
with open('Matches685.csv', 'rt') as csvfile:
    Data = csv.reader(csvfile, delimiter=',')
    next(Data)
    firstLine = True
    Sum685 = 0.0
    count685 = 0
    for row  in Data:
            Sum685 = Sum685 + float(row[8])
            count685 = count685 + 1
    print(Sum685/count685)

with open('Matches684.csv', 'rt') as csvfile:
    Data = csv.reader(csvfile, delimiter=',')
    next(Data)
    firstLine = True
    Sum685 = 0.0
    count685 = 0
    for row  in Data:
            Sum685 = Sum685 + float(row[8])
            count685 = count685 + 1

    print(Sum685/count685)

with open('Matches683.csv', 'rt') as csvfile:
    Data = csv.reader(csvfile, delimiter=',')
    next(Data)
    firstLine = True
    Sum685 = 0.0
    count685 = 0
    for row  in Data:
            Sum685 = Sum685 + float(row[8])
            count685 = count685 + 1

    print(Sum685/count685)

with open('Matches682.csv', 'rt') as csvfile:
    Data = csv.reader(csvfile, delimiter=',')
    next(Data)
    firstLine = True
    Sum685 = 0.0
    count685 = 0
    for row  in Data:
            Sum685 = Sum685 + float(row[8])
            count685 = count685 + 1

    print(Sum685/count685)

with open('Matches681.csv', 'rt') as csvfile:
    Data = csv.reader(csvfile, delimiter=',')
    next(Data)
    firstLine = True
    Sum685 = 0.0
    count685 = 0
    for row  in Data:
            Sum685 = Sum685 + float(row[8])
            count685 = count685 + 1

    print(Sum685/count685)
