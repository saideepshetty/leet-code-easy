
def oneEditAway(string1, string2):
    if len(string1) == len(string2):
        return checkReplacement(string1, string2)
    if len(string1) + 1 == len(string2):
        return checkInsertion(string1, string2)
    if len(string1) - 1 == len(string2):
        return checkInsertion(string2, string1)
    return False


def checkReplacement(string1, string2):
    foundReplacement = False
    for index, value in enumerate(string1):
        if string1[index] != string2[index]:
            if foundReplacement:
                return False
            else:
                foundReplacement = True
    return True

def checkInsertion(string1, string2):
    index1 = 0
    index2 = 0
    while index1 < len(string1) and index2 < len(string2):
        if string1[index1] != string2[index2]:
            if index1 != index2:
                return False
            else:
                index2 += 1
        else:
            index1 += 1
            index2 += 1
    return True

if __name__ == '__main__':
    string1 = 'apple'
    string2 = 'eppe'
    print(oneEditAway(string1, string2))
