import numpy as np

def valid(differences, firstPass):
    #0 difference => not increasing or decreasing
    if 0 in differences:
        if firstPass:
            return lenient_valid(differences)
        else:
            return False
    #differences must be either all increasing or all decreasing
    positives = [i for i in differences if i > 0]
    negatives = [j for j in differences if j < 0]
    if (len(positives) > 0 and len(negatives) > 0):
        if firstPass:
            return lenient_valid(differences)
        else:
            return False
    #differences must be 1 2 or 3
    absDiff = [abs(i) for i in differences]
    if (max(absDiff) > 3):
        if firstPass:
            return lenient_valid(differences)
        else:
            return False
    
    return True
    
def lenient_valid(differences):
    #only taking as input things which valid() has rejected
    #we want to see if we can remove ONE ELEMENT from the sequence to make it valid

    """
    if we have a sequence 1 3 2 4 5
    so differences 2 -1 2 1
    and we remove 3
    we get differences 1 2 1
    when we remove a difference we add the item we removed to the index before

    2 3 3 5
    1 0 2

    2 3 5
    1 2
    """

    if 0 in differences:
        removeIndex = differences.index(0)
        del differences[removeIndex]
        return valid(differences, firstPass=False)
    
    positives = [i for i in differences if i > 0]
    negatives = [j for j in differences if j < 0]

    if (len(negatives) > len(positives) and len(positives) > 1):
        return False
    if (len(positives) > len(negatives) and len(negatives) > 1):
        return False

    if (len(negatives) == 1):
        value = negatives[0]
        removeIndex = differences.index(value)
        del differences[removeIndex]
        if (removeIndex > 0):
            differences[removeIndex-1] += value
        return valid(differences, firstPass=False)

    if (len(positives) == 1):
        value = positives[0]
        removeIndex = differences.index(value)
        del differences[removeIndex]
        if (removeIndex > 0):
            differences[removeIndex-1] += value
        return valid(differences, firstPass=False)

    
    for i in range(len(differences)):
        value = differences[i]
        if (abs(value) > 3):
            del differences[i]
            if (i > 0):
                differences[i-1] += value
            return valid(differences, firstPass=False)

    return False

file = open("day2-input.txt","r")
lines = file.readlines()

safeCounter = 0

for line in lines:
    #trim newline character, split by space, map strings -> ints
    intLine = list(map(int, line[:-1].split(" ")))
    print(intLine)
    differences = list(np.diff(intLine))
    print(differences)

    if valid(differences, firstPass=True):
        safeCounter += 1

print(safeCounter)

file.close()