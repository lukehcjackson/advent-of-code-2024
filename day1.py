inputFile = open("day1-input.txt","r")

leftList = []
rightList = []

lines = inputFile.readlines()
for line in lines:
    #remove newline character
    line = line[:-1]
    pair = line.split("   ")
    leftList.append(int(pair[0]))
    rightList.append(int(pair[1]))

"""
distances = []
while len(leftList) > 0:
    leftSmallest = min(leftList)
    leftList.remove(leftSmallest)

    rightSmallest = min(rightList)
    rightList.remove(rightSmallest)

    distances.append(abs(leftSmallest - rightSmallest))

print(sum(distances))
"""

similarity = 0
for item in leftList:
    appearances = rightList.count(item)
    similarity += item * appearances

print(similarity)
