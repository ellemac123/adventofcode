"""
https://adventofcode.com/2023/day/4

the answer for part one is:  21213
"""


def matches(scratcher_list): 
    totals = 0

    for row in scratcher_list:
        count = 0
        for num in row[0]:
            if num in row[1]: 
                if not count:
                    count = 1
                else: 
                    count = count * 2
        
        totals = totals + count
    
    return totals

        


if __name__ == "__main__": 
    scratcher_list = []

    with open('input.txt', 'r') as f: 
        for a in f.readlines(): 
            line = a.strip().split(':')[1]
            one = line.split(' | ')

            first = [int(n) for n in one[0].strip().split()]
            sec = [int(n) for n in one[1].strip().split()]
            scratcher_list.append([first, sec])

    print('the answer for part one is: ', matches(scratcher_list))