"""
https://adventofcode.com/2024/day/10

Solution for day 10 part one: 482
Solution for day 10 part two: 1094
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

def check_each_trailhead(trailhead_map, trailhead_coordinates, part_two=False):
    """
    Given a map and coordinates of all the trailheads

    loop through the coordinates
    make a deep copy of the map since it will be modified by the coordinates
    it's modified because we only care that we can get to each 9
    not how many paths we can get there by

    increase total sum for each trailhead by the number of 9s it can reach
    """
    sum = 0
    for coordinate in trailhead_coordinates:
        map = copy.deepcopy(trailhead_map)
        row = coordinate[0]
        col = coordinate[1]
        value = map[row][col]

        # check each direction
        for direction in directions:
            sum += check(row + direction[0], col + direction[1], map, value, part_two)

    return sum

def check(row, col, map, prev_value, part_two):
    """
    Using recursion
    check that i am in bounds of the map
        if not return zero
    if yes
        check if I am a 9
            if yes
            set my location to X so i cannot be revisited by the same trailhead
            return a 1 to increase the number of peaks this trailhead can reach
        if not a 9
            check if i am one greater than my previous value
                if yes
                    check each direction recurrsively
                if no
                    return zero
    return sum of each direction ive travelled
    """
    if row < 0 or row >= len(map) or col < 0 or col >= len(map[0]):
        return 0
    current_value = map[row][col]

    if current_value == 9 and prev_value == 8:
        if not part_two:
            map[row][col] = 'X'
        return 1
    elif current_value != prev_value + 1:
        return 0
    else:
        # current value is + 1 greater than the previous value,
        # therefor traverse each direction
        paths = 0
        for direction in directions:
            next_row = row + direction[0]
            next_col = col + direction[1]
            paths += check(next_row, next_col, map, map[row][col], part_two)
    return paths

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        a = f.readlines()

    # part one
    trailhead_map = format_input(a)
    trailhead_coords = find_trailhead_positions(trailhead_map)
    trailhead_sums = check_each_trailhead(trailhead_map, trailhead_coords)
    trailhead_sums_two = check_each_trailhead(trailhead_map, trailhead_coords, part_two=True)


    print("Solution for day 10 part one:", trailhead_sums)
    print("Solution for day 10 part two:", trailhead_sums_two)