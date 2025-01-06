"""
The engine schematic (your puzzle input) consists of a visual
representation of the engine. There are lots of numbers and symbols
you don't really understand, but apparently any number adjacent to a
symbol, even diagonally, is a "part number" and should be included in
your sum. (Periods (.) do not count as a symbol.)

Of course, the actual engine schematic is much larger. What is the sum of all
the part numbers in the engine schematic?
"""
import re

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