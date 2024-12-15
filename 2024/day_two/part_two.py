# Prompt two part one 
# The engineers are trying to figure out which reports are safe. The Red-Nosed reactor 
# safety systems can only tolerate levels that are either gradually increasing or 
# gradually decreasing. 
# So, a report only counts as safe if both of the following are true:
# - The levels are either all increasing or all decreasing.
# - Any two adjacent levels differ by at least one and at most three.
# there were 463 in level 1
# 514 in level 2
import csv

inc_allowed = {1, 2, 3}
dec_allowed = {-1, -2, -3}
def main(): 
    inputDict = []

    safeList = []

    with open('input.txt') as inputText:
        input = csv.reader(inputText)

        for i in input:
            inputDict.append([int(val) for val in i[0].split(' ')])

    for checkList in inputDict: 
        if isSafe(checkList) or isSafeWithOneRemoved(checkList): 
            safeList.append(i)

    return len(safeList)
        

def isIncrementingOrDecrementing(inputRow, allowed_vals): 
    for i in range(len(inputRow)-1): 
        if inputRow[i+1] - inputRow[i] not in allowed_vals:
            return False
    return True

def isSafe(checkList): 
    if isIncrementingOrDecrementing(checkList, inc_allowed) or isIncrementingOrDecrementing(checkList, dec_allowed): 
        return True
    else: 
        return False
        

def isSafeWithOneRemoved(checkList): 
    for i in range(len(checkList)): 
        newList = checkList[:i] + checkList[i+1:]
        if isSafe(newList): 
            return True
    return False

if __name__ == "__main__": 
    print(main())