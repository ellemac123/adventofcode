"""
https://adventofcode.com/2023/day/5
"""

from collections import defaultdict


def format_input(): 
    """
    Semi format the input from the file
    """
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

def create_mapping(mapper): 
    """
    Given a slightly formatted dict, remove the seeds and 
    structure the lists so that they have the required ranges

    return a list of seeds and a dictionary of the other mappings
    """
    seeds = mapper['seeds']
    mapping_list = defaultdict(list)
    mapper.pop('seeds')

    for key in mapper.keys(): 
        mapping_list[key] = []
        for mapping in mapper[key]: 
            range_ = mapping[2]

            first = list(range(mapping[0], mapping[0] + range_))
            second = list(range(mapping[1], mapping[1] + range_))
            mapping_list[key].append([first, second])
    
    return seeds, mapping_list

def find_corresponding_values(seed, almanac): 
    totals = [seed]
    for i in almanac: 
        val = []
        for l in almanac[i]: 
            if seed in l[1]:
                seed_index = l[1].index(seed)
                seed = l[0][seed_index]
                val = seed
        if not val: 
            val = seed
        totals.append(val)
            
    return totals


def run(): 
    map_ = format_input()
    seeds, final_map = create_mapping(map_)

    for seed in seeds: 
        totals = find_corresponding_values(seed, final_map)
        print(totals)

if __name__ == "__main__": 
    run()