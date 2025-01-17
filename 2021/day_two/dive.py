"""
https://adventofcode.com/2021/day/2
answer for part one:  1427868
answer for part two:  1568138742

"""
DIRECTIONS = {
    'forward': (1, 0), 
    'down': (0, 1),
    'up': (0, -1)

}

AIM_MAP = {
    'up': 1, 
    'down': -1
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

def calculate_aim(depth_map): 
    """
    Aim Calculations: 
        down X increases your aim by X units.
        up X decreases your aim by X units.
        forward X does two things:
        It increases your horizontal position by X units.
        It increases your depth by your aim multiplied by X.
    """
    aim = 0
    position = [0,0]

    for line in depth_map: 
        calc = int(line[1])
        if line[0] in AIM_MAP.keys():
            aim += AIM_MAP[line[0]] * calc
        else: 
            position[0] += calc
            position[1] += (aim * calc)
    
    return position

def run(): 
    depth_map = []
    with open('input.txt', 'r') as f: 
        for line in f.readlines(): 
            depth_map.append(line.strip().split(' '))
    
    final_position = calculate_depth(depth_map)
    print('answer for part one: ', final_position[0]*final_position[1])

    final_aim = calculate_aim(depth_map)
    print('answer for part two: ', abs(final_aim[0]*final_aim[1]))


if __name__ == "__main__": 
    run()