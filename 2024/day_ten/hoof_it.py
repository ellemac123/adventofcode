"""
https://adventofcode.com/2024/day/10

Solution for day 10 part one: 482
"""
import copy
directions = [
    # row, col
    (0, 1), # right
    (0, -1), #left
    (1, 0), # up
    (-1, 0) # down
]

def format_input(input_string):
    """
    Given file_input of a list of strings, return
    a stripped list of lists
    """
    return [[int(val) for val in a.strip()] for a in input_string]

def find_trailhead_positions(map):
    """
    given a map return all list of tuple coords
    of zeros in the map. Zeros represent trailheads.
    """
    trailhead_coordinates = []
    for row, value in enumerate(map):
        if 0 in value:
            for col, letter in enumerate(value):
                if letter == 0:
                    trailhead_coordinates.append((row, col))

    return trailhead_coordinates

def check_each_trailhead(trailhead_map, trailhead_coordinates):
    """
    Given a map and coordinates of all the trailheads

    loop through the coodinates
    checking each trailhead to the end

    increase trailhead if direction has it
    """
    sum = 0
    for coordinate in trailhead_coordinates:
        map = copy.deepcopy(trailhead_map)
        row = coordinate[0]
        col = coordinate[1]
        value = map[row][col]

        # check each direction
        for direction in directions:
            sum += check(row + direction[0], col + direction[1], map, value)


    return sum


def check(row, col, map, prev_value):
    if row < 0 or row >= len(map) or col < 0 or col >= len(map[0]):
        return 0
    current_value = map[row][col]

    if current_value == 9 and prev_value == 8:
        map[row][col] = 'X'
        return 1

    elif current_value != prev_value + 1:
        return 0
    else:
        # current value is + greater than the previous value, traverse
        paths = 0
        for direction in directions:
            next_row = row + direction[0]
            next_col = col + direction[1]
            paths += check(next_row, next_col, map, map[row][col])
    return paths



if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        a = f.readlines()

    # part one
    trailhead_map = format_input(a)
    trailhead_coords = find_trailhead_positions(trailhead_map)
    trailhead_sums = check_each_trailhead(trailhead_map, trailhead_coords)

    print("Solution for day 10 part one:", trailhead_sums)