
def isAnagram(string1,string2):

    if sorted(string1) == sorted(string2):
        return True
    else:
        return False

def SortStringsIntoAnagrams(listOfStrings):

    templist = listOfStrings
    sortedList = []
    sortedList.append(listOfStrings[0])
    if len(templist) == 1:
        sortedList = sortedList + templist
    else:
        for firstString in templist:
            anagramLists = []


            for secondString in templist[1:]:

                if isAnagram(firstString,secondString):

                    anagramLists.append(secondString)
                    templist.remove(secondString)

            sortedList = sortedList + anagramLists

    return sortedList

def findElementSorted(sortedArray,upperLimit, lowerLimit, number):


    while (lowerLimit < upperLimit):

        mid = int((upperLimit + lowerLimit)/2)


def 
