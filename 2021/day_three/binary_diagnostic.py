"""
https://adventofcode.com/2021/day/3

the answer for part 1: 3882564
"""

from collections import defaultdict

def find_values(input_list): 
    binary = ''
    reverse_binary = ''
    for i in range(len(input_list[0])): 
        counter = defaultdict(int)
        for row in input_list: 
            counter[row[i]] += 1
        if counter[0] > counter[1]: 
            binary += '0'
            reverse_binary += '1'
        else: 
            binary += '1'
            reverse_binary += '0'


    power_consumption = int(binary, 2) * int(reverse_binary, 2)
    return power_consumption

def run(): 
    input_mapper = []
    with open('input.txt', 'r') as f: 
        for a in f.readlines(): 
            input_mapper.append([int(n) for n in a.strip()])

    power_consumption = find_values(input_mapper)
    print('the answer for part 1:', power_consumption)


if __name__ == "__main__": 
    run()