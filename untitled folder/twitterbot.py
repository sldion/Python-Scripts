import random



kanyeWestFile = open('kanyeWest.txt', 'rt')

dictionary = {}
for line in kanyeWestFile:
    x = line.split()
    for i in range(0, len(x) - 2):

        y = x[i:i + 3]
        if dictionary.get(x[0] + ' ' + x[1]) is not None:
            dictionary[x[0] + ' ' + x[1]].append(x[2])
        else:
            dictionary[x[0] + ' ' + x[1]] = [x[2]]


keys = dictionary.keys()

firstKey = keys[random.randint(0, len(keys) - 1)]
sentence = firstKey

while (len(sentence) < 140):

    newKey = ' '.join(sentence.split()[-2:])
    if dictionary.get(newKey) is None:
        break
    else:
        sentence += ' ' + dictionary[newKey][random.randint(0, len(dictionary[newKey] ) - 1)]

print sentence
