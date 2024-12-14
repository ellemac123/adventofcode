# day one - prompt: 
# Within each pair, figure out how far apart the two numbers are; 
# you'll need to add up all of those distances. For example, if you 
# pair up a 3 from the left list with a 7 from the right list, the distance 
# apart is 4; if you pair up a 9 with a 3, the distance apart is 6.
import csv

def main(): 
    listone = []
    listtwo = []
    with open('input.txt') as inputFile: 
        # using the file provided, put the input into two lists
        for a in csv.reader(inputFile): 
            item = a[0].split('   ')
            listone.append(int(item[0]))
            listtwo.append(int(item[1]))

    if len(listone) != len(listtwo): 
        return 'list one and list two are not the same lengths'

    listone.sort()
    listtwo.sort()

    distance = []

    for i in range(len(listone)): 
        # the lists are the same so append the distance of 
        # the absolute value between one and two
        distance.append(abs(listone[i] - listtwo[i]))
    return sum(distance)


if __name__ == '__main__': 
    main()