# Prompt two part one 
# The engineers are trying to figure out which reports are safe. The Red-Nosed reactor 
# safety systems can only tolerate levels that are either gradually increasing or 
# gradually decreasing. 
# So, a report only counts as safe if both of the following are true:
# - The levels are either all increasing or all decreasing.
# - Any two adjacent levels differ by at least one and at most three.
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

    for i in inputDict: 
        if isIncrementingOrDecrementing(i, inc_allowed) or isIncrementingOrDecrementing(i, dec_allowed): 
            safeList.append(i)

    return len(safeList)
        

def isIncrementingOrDecrementing(inputRow, allowed_vals): 
    for i in range(len(inputRow)-1): 
        if inputRow[i+1] - inputRow[i] not in allowed_vals:
            return False
    return True

if __name__ == "__main__": 
    print(main())