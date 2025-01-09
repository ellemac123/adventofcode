"""
The engine schematic (your puzzle input) consists of a visual
representation of the engine. There are lots of numbers and symbols
you don't really understand, but apparently any number adjacent to a
symbol, even diagonally, is a "part number" and should be included in
your sum. (Periods (.) do not count as a symbol.)

Of course, the actual engine schematic is much larger. What is the sum of all
the part numbers in the engine schematic?
"""
import math
import re
from functools import reduce

DIRECTIONS = [
    # row, col
    (0, 1), # to the right
    (0, -1), # to the left
    (1, 0), # up
    (-1, 0), # down
    (1, 1), # up right diag
    (1, -1), # down right diag
    (-1, 1), # left up diag
    (-1, -1) # left down diag
]

def find_symbols(input, special_chars):
    digit_list = []
    for row in range(len(input)):
        for col in range(len(input[row])):
            flag = False
            try:
                if input[row][col] not in special_chars and input[row][col] != '.':
                    for i in DIRECTIONS:
                        new_row = row + i[0]
                        new_col = col + i[1]
                        if new_row < 0 or new_row >= len(input) or new_col < 0 or new_col >= len(input[0]):
                            continue
                        elif input[new_row][new_col] in special_chars:
                            flag = True
            except:
                continue
            if flag:
                digit_list.append((int(row), int(col)))
    return digit_list


def find_matches(digits, file_input):
    """
        given a list of digit coordinates
        recursively check if there are any numbers to the left of it
        if there are set tht to "X" and return the original number

        once that is all returned
        check if there's any to the left
        if there are set to "X" and return
    """
    new_digit_list = [list(row) for row in file_input]
    file_input = new_digit_list
    finals = []
    for i in range(len(digits)):
        digit = ''
        location_x = digits[i][0]
        location_y = digits[i][1]
        while True:
            if location_y < 0 or not file_input[location_x][location_y].isdigit():
                break
            else:
                digit = file_input[location_x][location_y] + digit
                file_input[location_x][location_y] = 'X'
                location_y = location_y - 1

        location_y = digits[i][1] + 1
        while True:
            if location_y > len(file_input[location_x]) or not file_input[location_x][location_y].isdigit():
                break
            else:
                digit = digit + file_input[location_x][location_y]
                file_input[location_x][location_y] = 'X'
                location_y = location_y + 1
        if digit:
            finals.append(digit)


    integer_numbers = [int(dig) for dig in finals]
    return integer_numbers


def get_partial_number(location_y, row):
    old_loc = location_y
    digit = ''
    while True:
        if location_y < 0 or not row[location_y].isdigit():
            break
        else:
            digit = row[location_y] + digit
            location_y = location_y - 1
    location_y = old_loc + 1
    while True:
        if location_y > len(row) or not row[location_y].isdigit():
            break
        else:
            digit = digit + row[location_y]
            location_y = location_y + 1
    if digit:
        return int(digit)



def find_part_two_items(input):
    """
    Find each gear and return its part number.
    A gear is any * symbol that is adjacent to exactly two part numbers.
    Its gear ratio is the result of multiplying those two numbers together.
    """
    new_digit_list = [list(row) for row in input]

    star_locations = []
    for row in range(len(new_digit_list)):
        if '*' in new_digit_list[row]:
            # if there is a star in the row
            for val in range(len(new_digit_list[row])):
                # loop through the row bec there might be a lot of stars
                if new_digit_list[row][val] == '*':
                    # if the value is a star
                    multiply_vals = set()
                    for x in DIRECTIONS:
                        if new_digit_list[row + x[0]][val + x[1]].isdigit():
                            # check there are digits near it
                            # get part number
                            multiply_vals.add(get_partial_number(val + x[1], new_digit_list[row + x[0]]))

                    # add digits loc to a list
                    # if length of values is > 1 at the end
                    # add all that to the main list
                    if len(multiply_vals) > 1:
                        star_locations.append(multiply_vals)
    return star_locations

def sum_set(locations):
    """
    Suboptimal but get the product of each set
    and return the sum of all the products
    """
    finals = []

    for i in locations:
        mult = 1
        for val in i:
            mult *= val
        if mult > 1:
            finals.append(mult)

    return sum(finals)

if __name__ == "__main__":
    """
    Read file
    Grab all non-digit and non-period special characters
    """
    file_input = []
    special_characters = set()
    regex = r"[^0-9.]"
    with open('input.txt', 'r') as f:
        input = f.readlines()
        for row in input:
            file_input.append(row)
            special_characters.update([a for a in re.findall(regex, row)])

    special_characters.remove('\n')

    digits = find_symbols(file_input, special_characters)
    matches = find_matches(digits, file_input)
    print("the solution for round 1 is: ", sum(matches))

    items = find_part_two_items(file_input)
    print("the solution for round 1 is: ", sum_set(items))