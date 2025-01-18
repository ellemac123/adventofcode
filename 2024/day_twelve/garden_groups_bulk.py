"""
https://adventofcode.com/2024/day/12

this is currently working for all "outer corners" 
"""
from collections import Counter, defaultdict

DIRECTIONS = [
    (-1, 0),  # up
    (1, 0),  # down
    (0, 1),  # right
    (0, -1),  # left
]

CORNER = [
    # right upper corner
    [1, 1], 
    [-1, -1]
    # left upper corner
    # right lower corner
    # left lower corner
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
                    #row: [directions checked
                    _, area, perim = find_touching(val, input_list, row_num, col_num)
                    finals.append([val, area, perim])
    
    # not perimiter returns the checked boundary    
    return finals

def find_corners(checked_locations): 
    """
        Given a list of checked values for perimeters

        find all the corners
        a corner is where we have the same column but 1 row seperated either up or down AND
        same row and 1 col left or right 
    """
    final_ = []
    for locations in checked_locations: 
        print(locations)
        checked = [list(t) for t in locations[2]]
        corners = 0
        for spot in checked: 
            # check corners
            row = spot[0]
            col = spot[1]
            for corner in CORNER: 
                corner_row = corner[0]
                corner_col = corner[1]
                # take my location and look for +1 +1 

                check_me = [row+corner_row, col+corner_col]
                if check_me in checked: 
                    corners += 1
            # check row
            # check col

            # create a list with new count and area and letter
        final_.append([locations[0], locations[1], corners])

    for xi in final_: 
        print(xi)
    
    return final_        

"""
TODO:
I think we might be able to just check corners and add to a list within the find_touchng !!
"""


def find_touching(letter, input_list, row_num, col_num):
    """
    Given a letter, input_list and location

    letter in position == letter
        increase area by 1

    check all 4 directions
        if the letter is touching in any direction, traverse that direction
        else add row, col to the bulk_fencing list
    
    
    after all that set it to its numerical ordenance

    return updated input_list, perimeter, area
    """
    area = 0
    perimeter = set()
    set_letter = ord(letter) - 97
    if letter == input_list[row_num][col_num]:
        area = area + 1
        input_list[row_num][col_num] = set_letter
        for direction in DIRECTIONS:
            check_row = row_num + direction[0]
            check_col = col_num + direction[1]
            check = (check_row < 0 or check_col < 0 or check_row >= len(input_list) or check_col >= len(input_list[0]))
            if check:
                perimeter.add((check_row, check_col))
            elif input_list[check_row][check_col] != letter and input_list[check_row][check_col] != set_letter:
                perimeter.add((check_row, check_col))
            elif input_list[check_row][check_col] == letter:
                input_list, searched_area, searched_perimeter = find_touching(letter, input_list, check_row, check_col)
                area = area + searched_area
                perimeter.update(searched_perimeter)

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
    with open('tiny_example.txt', 'r') as f:
        for line in f.readlines(): 
            input_list.append(list(line.strip()))

    final_traverse = traverse_letters(input_list)

    corners = find_corners(final_traverse)

    # sum_values = sum_vals(final_traverse)

    # print('the answer for part two is: ', sum_values)