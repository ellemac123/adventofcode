# Prompt two part one 
# The engineers are trying to figure out which reports are safe. The Red-Nosed reactor 
# safety systems can only tolerate levels that are either gradually increasing or 
# gradually decreasing. 
# So, a report only counts as safe if both of the following are true:
# - The levels are either all increasing or all decreasing.
# - Any two adjacent levels differ by at least one and at most three.
import csv

def main(): 
    inputDict = []

    safeList = []

    with open('input.txt') as inputText:
        input = csv.reader(inputText)

        for i in input:
            inputDict.append(i[0].split(' '))

    for i in inputDict: 
        if isDecrementing(i) or isIncrementing(i): 
            print(i)
            safeList.append(i)

    return len(safeList)
        


def isDecrementing(inputRow): 
    for i in range(len(inputRow)-1): 
        diff = int(inputRow[i+1]) - int(inputRow[i])
        if (diff > 3 or diff < 1):
            return False
    return True

def isIncrementing(inputRow):  
    for i in range(len(inputRow)-1): 
        diff = int(inputRow[i+1]) - int(inputRow[i])
        if (diff < -3 or diff >= 0): 
            return False
    return True


if __name__ == "__main__": 
    print(main())