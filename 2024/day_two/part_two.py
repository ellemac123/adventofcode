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

    for i in inputDict: 
        if isDecrementing(i) or isIncrementing(i): 
            safeList.append(i)

    return len(safeList)
        

def isIncrementing(inputRow): 
    removal = 0
    for i in range(len(inputRow)-1): 
        diff = inputRow[i+1] - inputRow[i]
        
        if diff not in inc_allowed:
            if removal == 0: 
                if i == 0: 
                    removal += 1
                    continue
                elif i == len(inputRow)-2: 
                     return True
                else: 
                    if len(inputRow) > i+1 and i > 0:
                        diff = inputRow[i+1] - inputRow[i-1]
                        if 3 >= diff >= 1: 
                            removal += 1
                            continue
                        else: 
                            return False
                    else: 
                        return False
            else: 
                return False
    return True


def isDecrementing(inputRow):  
    removal = 0
    for i in range(len(inputRow)-1):         
        diff = inputRow[i+1] - inputRow[i]
        if diff not in dec_allowed: 
            # if no items have been "removed" yet
            if removal == 0: 
                # if its the first index
                if i == 0: 
                    removal = removal + 1 
                    continue
                
                # if its the second to last and nothing
                # has been removed, "remove" the last one
                if (i == len(inputRow) - 2): 
                    return True
                else: 
                    if len(inputRow) > i+1 and i > 0:
                        diff = inputRow[i+1] - inputRow[i-1]
                        if -3 <= diff <= -1: 
                            removal = removal + 1 
                            continue
                        else:      
                            return False 
                    else: 
                        return False
            else: 
                return False
    return True


if __name__ == "__main__": 
    print(main())