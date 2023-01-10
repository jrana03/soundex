# COMP 1026 - Assignment 2
# Jai Rana (jrana23)
# soundex program to convert each name in a given list to its respective soundex encoding

names = []
encodedPairs = []


def userNames():  # Function 1 - list of names from user input
    """
    userNames receives input from the user to create a list of names
    :return: list of names
    """
    print('Enter names, one on each line. Type DONE to quit entering names.')
    while True:
        userInp = input()
        if userInp != 'DONE':
            names.append(userInp)
        else:
            return names


def replaceDigits(word):  # Function 2 - replacing letters with digits
    """
    replaceDigits takes a word as a parameter and converts the letters to soundex encoding digits
    :param word: word received as the input to convert to digits
    :return: word with replaced letters as the encoded digits
    """
    soundex = ''
    for ch in word:
        if ch in ['a', 'e', 'i', 'o', 'u', 'y', 'h', 'w']:
            soundex += '0'
        elif ch in ['b', 'f', 'p', 'v']:
            soundex += '1'
        elif ch in ['c', 'g', 'j', 'k', 'q', 's', 'x', 'z']:
            soundex += '2'
        elif ch in ['d', 't']:
            soundex += '3'
        elif ch in ['l']:
            soundex += '4'
        elif ch in ['m', 'n']:
            soundex += '5'
        elif ch in ['r']:
            soundex += '6'
    return soundex


def removeDuplicatesandZeros(digits):  # Function 3 - removing the duplicate digits and zeros
    """
    removeDuplicatesandZeros removes consecutive repeated digits and removes 0s from the encoded word
    :param digits: the digits encoded from the soundex function
    :return: noZeros is the value of encoded digits without repeated consecutive values nor 0s
    """
    noDuplicates = ''
    noZeros = ''
    for i in range((len(digits))):
        if i == 0:
            noDuplicates += digits[i]
        elif digits[i] != noDuplicates[-1]:
            noDuplicates += digits[i]
    for j in noDuplicates:
        if j != '0':
            noZeros += j
    return noZeros


def checkLength(D):  # Function 4 - ensuring the length is 4
    """
    checkLength ensured the encoded digits is not higher than the length of 4
    :param D: D is the encoded digits without repeated values and without 0s
    :return: returns a value with length 4 and 0s making up the missing length
    """
    if len(D) == 4:
        pass
    elif len(D) < 4:
        D += '0' * (4 - len(D))
    elif len(D) > 4:
        D = D[:4]
    return D


def soundex(word): # Function 5 - entire soundex algorithm
    """
    soundex function runs through the entire soundex algorithm to convert names to digits properly with the first letter
    :param word: word parameter is the name in each list
    :return: D is returned as a final encoded value of each name
    """
    word = word.lower()
    for i in range(len(word)):
        firstLetter = word[0]
    rawSoundex = replaceDigits(word)
    for i in range(len(rawSoundex)):
        firstDigit = rawSoundex[0]
    editedSoundex = removeDuplicatesandZeros(rawSoundex)
    if len(editedSoundex) > 0:
        for i in range(len(editedSoundex)):
            firstDigit_edited = editedSoundex[0]
        if firstDigit != firstDigit_edited:
            editedSoundex = firstLetter + editedSoundex
        elif firstDigit == firstDigit_edited:
            editedSoundex = firstLetter + editedSoundex[1:]
    else:
        editedSoundex = firstLetter
    D = checkLength(editedSoundex)
    return D


def main(): # Function 6 - main function
    """
    main function executes all previous functions while organizing and giving a valid output
    :return: returns output list of pairs of soundex digits and names
    """
    userNames()
    for word in names:
        encodedName = (soundex(word))
        myTuple = (encodedName, word)
        encodedPairs.append(myTuple)
    outputList = []
    for i in range(len(encodedPairs)):
        for j in range(len(encodedPairs)):
            if i != j:
                if encodedPairs[i][0] == encodedPairs[j][0]:
                    namesMin = min(encodedPairs[i][1], encodedPairs[j][1])
                    namesMax = max(encodedPairs[i][1], encodedPairs[j][1])
                    if (f'{namesMin} and {namesMax} have the same Soundex encoding.') not in outputList:
                        outputList.append(f'{namesMin} and {namesMax} have the same Soundex encoding.')
    outputList.sort()
    for pair in outputList:
        print(pair)
    return outputList


main()
