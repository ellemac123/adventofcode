# Prompt: This time, you'll need to figure out exactly how often
# each number from the left list appears in the right list.
# Calculate a total similarity score by adding up each number in the left
# list after multiplying it by the number of times that number 
# appears in the right list. eg: the number is 3 and it is in the other 
# list 2 times; score is 3 * 2 = 6
import csv
from collections import Counter

def main(): 
    listone = []
    listtwo = []
    distance = []

    with open('input.txt') as inputFile: 
        # using the file provided, put the input into two lists
        for a in csv.reader(inputFile): 
            item = a[0].split('   ')
            listone.append(int(item[0]))
            listtwo.append(int(item[1]))

    if len(listone) != len(listtwo): 
        return 'list one and list two are not the same lengths'

    listone.sort()
    listtwo = Counter(listtwo)
    
    for i in range(len(listone)): 
        # use the current value in list one and 
        # get the count in list two by making it the key
        value = listone[i] * listtwo[listone[i]]
        distance.append(value)

    return sum(distance)


if __name__ == '__main__': 
    print(main())




