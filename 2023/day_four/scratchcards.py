"""
https://adventofcode.com/2023/day/4

the answer for part one is:  21213
the answer for part two is:  8549735
"""
from collections import defaultdict, Counter

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


def scratchcard_copies(scratcher_list): 
    """
    Create a counter of the scratch cards

    loop through the cards and increment their count

    return dictionary of copies
    """
    copies = {i:1 for i in range(len(scratcher_list))}

    for row_iteration, row in enumerate(scratcher_list): 
        match_counter = 1
        for number in row[0]: 
            if number in row[1]: 
                copies[row_iteration + match_counter] += 1*copies[row_iteration]
                match_counter += 1
    
    return copies


def count_scratchers(scratch_dict): 
    """
    Sum scratchcards in dictionary
    """
    sum = 0 
    for i in scratch_dict.keys():
        sum += scratch_dict[i]

    return sum


if __name__ == "__main__": 
    """
    Format the list and run the code for part one and two
    """

    scratcher_list = []

    with open('input.txt', 'r') as f: 
        for a in f.readlines(): 
            line = a.strip().split(':')[1]
            one = line.split(' | ')

            first = [int(n) for n in one[0].strip().split()]
            sec = [int(n) for n in one[1].strip().split()]
            scratcher_list.append([first, sec])

    print('the answer for part one is: ', matches(scratcher_list))

    # part two
    scratch_counts = scratchcard_copies(scratcher_list)
    print('the answer for part two is: ', count_scratchers(scratch_counts))