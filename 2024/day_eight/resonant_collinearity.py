"""
https://adventofcode.com/2024/day/8
"""
from itertools import product

def find_difference(coordinates_set, puzzle_input):
    # find the difference between two cartesian products
    extra_set = set()
    coord_one = coordinates_set[0]
    coord_two = coordinates_set[1]
    if coord_one == coord_two:
        # if its 0 0 ignore
        return puzzle_input, extra_set

    # otherwise add that to the first one
    diff = (coord_one[0] - coord_two[0], coord_one[1] - coord_two[1])

    if diff[0] <= 0:
        if coord_one[0] + diff[0] >= 0 and coord_one[1] + diff[1] >= 0:
            try:
                if puzzle_input[coord_one[0] + diff[0]][coord_one[1] + diff[1]] == '.':
                    puzzle_input[coord_one[0] + diff[0]][coord_one[1] + diff[1]] = "#"
                extra_set.add((coord_one[0] + diff[0], coord_one[1] + diff[1]))
            except IndexError:
                pass
        if coord_two[0] - diff[0] >= 0 and coord_two[1] - diff[1] >= 0:
            try:
                if puzzle_input[coord_two[0] - diff[0]][coord_two[1] - diff[1]] == '.':
                    puzzle_input[coord_two[0] - diff[0]][coord_two[1] - diff[1]] = "#"
                extra_set.add((coord_two[0] - diff[0], coord_two[1] - diff[1]))
            except IndexError:
                pass
    return puzzle_input, extra_set

def find_resonant_collinearity(puzzle_input, unique_resonances):
    # create a set of coords that arent going to be transformed to #
    hidden_resonance_coordinates = set()
    cartesian_product = dict()

    for value in unique_resonances:
        cartesian_product[value] = list(product(unique_resonances[value], repeat=2))

    for i in cartesian_product:
        for j in range(len(cartesian_product[i])):
            diff, others = find_difference(cartesian_product[i][j], puzzle_input)
            hidden_resonance_coordinates.update(others)

    return len(hidden_resonance_coordinates)

if __name__ == "__main__":
    input = []
    # create a dictionary of resonances and their coordinates
    unique_values = dict()
    with open('input.txt', 'r') as infile:
        row = 0
        for i in infile:
            line = list(i.strip())
            for val in range(len(line)):
                if line[val] != '.':
                    unique_values.setdefault(line[val], []).append((row, val))
            input.append(line)
            row = row+1

    coords = find_resonant_collinearity(input, unique_values)

    print("The solution for part 1 is:", coords )

