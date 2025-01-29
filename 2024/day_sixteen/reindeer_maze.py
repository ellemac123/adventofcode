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


def recursive_move(map, position): 
    for direction in DIRECTIONS: 
        if map[position[0]+ direction[0]][position[1]+direction[1]] == '.': 
            # set the location to a "-"
            # move to the next posision using recursion
            map[position[0]][position[1]] = '^'
            position = (position[0]+ direction[0], position[1]+direction[1])
            map[position[0]][position[1]] = 'S'
            val = recursive_move(map, position)
            if val:
                return val + 1
        elif map[position[0]+ direction[0]][position[1]+direction[1]] == 'E': 
            return 1


def move(map):
    """

    """ 
    moves = -1
    start, end = find_start_location(map)
    print(start, end)
    
    position = start[:]
    print(position)

    total = recursive_move(map, position)
    print(total)

        
    
    for a in map: 
        print(a)

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