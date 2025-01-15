"""
https://adventofcode.com/2024/day/12
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

def calc_perimiter(input_list, unique_letters): 
    """
    Given an input_list
    and a list of unique letters

    loop through the unique letters list
    loop through each row
        check if the letter == unique letter we are searching for
        if yes
            check each side of the letter
            if the side ISNT the same letter
            incrememnt count by 1
        else
            continue

    """
    perimiter = defaultdict(int)

    for letter in unique_letters: 
        perimiter[letter] = 0
        for row_num, row in enumerate(input_list): 
            if letter in row: 
                for col_num, row_value in enumerate(row):
                    if row_value == letter:
                        for direction in DIRECTIONS: 
                            try:
                                check_row = row_num + direction[0]
                                check_col = col_num + direction[1]
                                # check if the next spot is out of bounds
                                check = (check_row < 0 or check_col < 0)
                                if row_value != input_list[check_row][check_col] or check:
                                    perimiter[row_value] += 1
                            except IndexError: 
                                # if there is an out of bounds next to it that counts as a perimiter!
                                perimiter[row_value] += 1
    print(perimiter)
    return perimiter


def calculate_area_params(area_dict, parameter_dict): 
    sum = 0
    for letter in area_dict.keys(): 
        sq_footage = area_dict[letter] * parameter_dict[letter]
        sum = sum + sq_footage

    return sum 



if __name__ == '__main__':
    input_list = []
    with open('input.txt', 'r') as f:
        for line in f.readlines(): 
            input_list.append(list(line.strip()))

    area = get_area_for_each(input_list)
    # keys should contain all the unique letters in the counter
    parameters = calc_perimiter(input_list, area.keys())

    print('Answer for part one: ', calculate_area_params(area, parameters))