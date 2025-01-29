"""
https://adventofcode.com/2024/day/16
"""

DIRECTIONS = [
    (1, 0), 
    (0, 1), 
    (-1, 0), 
    (0, -1),
]

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
    print(map)

if __name__ == "__main__": 
    run()