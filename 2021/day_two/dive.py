"""
https://adventofcode.com/2021/day/2
answer for part one:  1427868
"""
DIRECTIONS = {
    'forward': (1, 0), 
    'down': (0, 1),
    'up': (0, -1)

}

def calculate_depth(depth_map): 
    """
        With a starting position of zero zero 
        calculate using your map your end position
    """
    position = [0,0]

    for line in depth_map: 
        calc = int(line[1])
        direction = DIRECTIONS[line[0]]

        position[0] += (direction[0] * calc)
        position[1] += (direction[1] * calc)
    
    return position


def run(): 
    depth_map = []
    with open('input.txt', 'r') as f: 
        for line in f.readlines(): 
            depth_map.append(line.strip().split(' '))
    
    final_position = calculate_depth(depth_map)

    print('answer for part one: ', final_position[0]*final_position[1])


if __name__ == "__main__": 
    run()