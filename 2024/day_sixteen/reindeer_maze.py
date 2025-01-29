"""
https://adventofcode.com/2024/day/16
"""

DIRECTIONS = [
    (1, 0), 
    (0, 1), 
    (-1, 0), 
    (0, -1),
]


def find_start_location(map): 
    start = ()
    end = ()
    for x, line in enumerate(map): 
        if 'S' in line: 
            start = (x, line.index('S'))
        if 'E' in line: 
            end = (x, line.index('E'))
    
    return start, end

def move(map):
    """

    """ 
    start, end = find_start_location(map)
    print(start, end)


def create_map(): 
    """
    Read the input file and add to a map list
    return map
    """
    map = []
    with open('tiny_input.txt', 'r') as f: 
        for line in f.readlines(): 
            map.append(list(line.strip()))
    
    return map

def run(): 
    """
    Run this all! 
    """
    map = create_map()
    move(map)

if __name__ == "__main__": 
    run()