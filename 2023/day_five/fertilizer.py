"""
https://adventofcode.com/2023/day/5
"""

from collections import defaultdict

def format_input(): 
    maps = defaultdict(list)
    temp = []
    with open('tiny_input.txt', 'r') as f: 
        for line in f.readlines(): 
            if line.startswith('seeds: '): 
                maps['seeds'] = [int(seed) for seed in line.split(': ')[1].split(' ')]
            elif line == '\n' and temp: 
                maps[temp[0]] = temp[1:]
                temp = []
            elif line != '\n':
                if temp:
                    temp.append([int(a) for a in line.strip().split(' ')])
                else: 
                    temp.append(line.strip().split(' ')[0])  
    return maps

def run(): 
    map_ = format_input()
    for a in map_: 
        print(a)

if __name__ == "__main__": 
    run()