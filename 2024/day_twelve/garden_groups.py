"""
https://adventofcode.com/2024/day/12

the answer for part one is:  1477762
"""
from collections import Counter, defaultdict

DIRECTIONS = [
    (-1, 0),  # up
    (1, 0),  # down
    (0, 1),  # right
    (0, -1),  # left
]

def get_area_for_each(input_list):
    """
    Given an input list containing rows of letters

    get a count of how many letters there are in each

    return area count
    """
    letters_area = Counter()
    for line in input_list:
        letters_area.update(line)

    return letters_area


def traverse_letters(input_list):
    letters_remaining = set(get_area_for_each(input_list))
    """   
    loop through the list
    for each row, check each value and see if its not a digit
    
    if not - find all touching it
    """
    finals = []
    for row_num, row in enumerate(input_list):
        if any(letter in letters_remaining for letter in row):
            for col_num, val in enumerate(row):
                if val in letters_remaining:
                    _, perim, area = find_touching(val, input_list, row_num, col_num)
                    finals.append([val, perim, area])
    return finals



def find_touching(letter, input_list, row_num, col_num):
    """
    Given a letter, input_list and location

    letter in position == letter
        increase area by 1

    check all 4 directions
        if the letter is touching in any direction, traverse that direction
        else
            increment parameter by 1

    after all that set it to its numerical ordenance

    return updated input_list, perimeter, area
    """
    area = 0
    perimeter = 0
    set_letter = ord(letter) - 97

    if letter == input_list[row_num][col_num]:
        area = area + 1
        input_list[row_num][col_num] = set_letter
        for direction in DIRECTIONS:
            check_row = row_num + direction[0]
            check_col = col_num + direction[1]
            check = (check_row < 0 or check_col < 0 or check_row >= len(input_list) or check_col >= len(input_list[0]))
            if check:
                perimeter = perimeter + 1
            elif input_list[check_row][check_col] != letter and input_list[check_row][check_col] != set_letter:
                perimeter = perimeter + 1
            elif input_list[check_row][check_col] == letter:
                input_list, searched_area, searched_perimeter = find_touching(letter, input_list, check_row, check_col)
                area = area + searched_area
                perimeter = perimeter + searched_perimeter

    return input_list, area, perimeter

def sum_vals(input):
    """
    Return the product of all the sums of the lines
    """
    totals = defaultdict(int)
    sum_ = 0

    for line in input:
        totals[line[0]] += line[1] * line[2]

    for keys in totals.keys():
       sum_ = sum_ + totals[keys]

    return sum_


if __name__ == '__main__':
    input_list = []
    with open('input.txt', 'r') as f:
        for line in f.readlines(): 
            input_list.append(list(line.strip()))



    final_traverse = traverse_letters(input_list)
    sum_values = sum_vals(final_traverse)

    print('the answer for part one is: ', sum_values)