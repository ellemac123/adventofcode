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
                    print()
                    print('letter:', val)
                    _, area, perim = find_touching(val, input_list, row_num, col_num)
                    finals.append([val, area, perim])

    return finals


"""
what is a corner? 

Traditional Corners [DONE!]: 
A corner is when there is no one above me or next to me to the right direction
or 
A corner is when there is no one below me or next to me to the right direction
or 
A corner is when there is no one above me or next to me to the left direction
or 
A corner is when there is no one below me or next to me to the left direction

Internal Corners: 
An internal corner is when there is someone above me and to the right of me, but not to the right 1 and above 1
or 
...
"""

TRADITIONAL_CORNER = [
    # A corner is when there is no one above me or next to me to the right direction
    [(-1, 0), (0, 1)], 
    # # A corner is when there is no one below me or next to me to the right direction
    [(1, 0), (0, 1)],
    # A corner is when there is no one above me or next to me to the left direction
    [(-1, 0), (0, -1)], 
    # A corner is when there is no one below me or next to me to the left direction
    [(1, 0), (0, -1)], 
]

INTERNAL_CORNERS = [
# An internal corner is when there is someone above me and to the right of me, but not to the right 1 and above 1
    [(-1, 0), (0, 1), (-1, 1)]
]


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
    corners = 0
    set_letter = ord(letter) - 97
    if letter == input_list[row_num][col_num]:
        area = area + 1
        input_list[row_num][col_num] = set_letter
        
        for corner in TRADITIONAL_CORNER: 
            checker = True
            #row check
            row_check_x = row_num + corner[0][0]
            row_check_y = col_num + corner[0][1]
            # check the row_check is either oob or not a letter
            # if not set checker to False
            try: 
                check = (row_check_x < 0 or row_check_y < 0 or row_check_x >= len(input_list) or row_check_y >= len(input_list[0]))
                if not check and (letter == input_list[row_check_x][row_check_y] or set_letter == input_list[row_check_x][row_check_y]): 
                    checker = False
            except IndexError: 
                pass
            #col check 
            col_check_x = row_num + corner[1][0]
            col_check_y = col_num + corner[1][1]

            # check the col_check is either oob or not a letter
            # if not set checker to False
            try: 
                check = (col_check_x < 0 or col_check_y < 0 or col_check_x >= len(input_list) or col_check_y >= len(input_list[0]))
                if not check and (letter == input_list[col_check_x][col_check_y] or set_letter == input_list[col_check_x][col_check_y]): 
                    checker = False
            except IndexError: 
                pass
            
            if checker: 
                corners += 1
        
        
        for internal_corner in INTERNAL_CORNERS: 
            checker = False
            row_check_x = row_num + internal_corner[0][0]
            row_check_y = col_num + internal_corner[0][1]

            col_check_x = row_num + internal_corner[1][0]
            col_check_y = col_num + internal_corner[1][1]


            not_value_x = row_num + internal_corner[2][0]
            not_value_y = col_num + internal_corner[2][1]

            # if not values are out of bounds dont do anything
            check = (not_value_x < 0 or not_value_y < 0 or not_value_x >= len(input_list) or not_value_y >= len(input_list[0]))
            if not check and (input_list[not_value_x][not_value_y] not in [letter, set_letter]): 
                if input_list[row_check_x][row_check_y] in [letter, set_letter] and input_list[col_check_x][col_check_y] in [letter, set_letter]:
                    checker = True
                # if we arent out of bounds and the letter in the value is not the letter of set_letter
                # we can assume the others exist
            
            if checker: 
                corners += 1
                
        for direction in DIRECTIONS:
            check_row = row_num + direction[0]
            check_col = col_num + direction[1]
            check = (check_row < 0 or check_col < 0 or check_row >= len(input_list) or check_col >= len(input_list[0]))
            if not check and input_list[check_row][check_col] == letter:
                input_list, searched_area, searched_corners = find_touching(letter, input_list, check_row, check_col)
                area += searched_area
                corners += searched_corners

    return input_list, area, corners


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
    with open('tiny_input.txt', 'r') as f:
        for line in f.readlines(): 
            input_list.append(list(line.strip()))

    final_traverse = traverse_letters(input_list)
    print(final_traverse)

    # sum_values = sum_vals(final_traverse)

    # print('the answer for part two is: ', sum_values)