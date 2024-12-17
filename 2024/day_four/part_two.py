"""
Looking for the instructions, you flip over the word search to find that this isn't actually
an XMAS puzzle; it's an X-MAS puzzle in which you're supposed to find two MAS in the shape of
an X. One way to achieve that is like this:

M.S
.A.
M.S

answer: 1902
"""
import re

MATCH = "MAS"
MATCH2 = "SAM"


def check_if_match(up_values): 
    if up_values == MATCH or up_values == MATCH2:
        return True
    else: 
        return False


def check_right_diagnol(rows, current_row, current_position): 
    #check 3 in the up right direction
    try:    
        if current_row - 1 < 0 or current_position - 1 < 0: 
            return False
        up_values = rows[current_row - 1][current_position - 1] + rows[current_row][current_position] + rows[current_row + 1][current_position + 1]
        
        return check_if_match(up_values)
    except IndexError: 
        return False

def check_left_diagnol(rows, current_row, current_position): 
    #check 3 in the down left direction
    try:    

        if current_row - 1 < 0 or current_position - 1 < 0: 
            return False

        up_values = rows[current_row + 1][current_position - 1] + rows[current_row][current_position] + rows[current_row - 1][current_position + 1]
        return check_if_match(up_values)
    except IndexError: 
        return False


def check_X_MAS(rows): 
    count = 0
    for row_value in range(len(rows)): 
        for letter_value in range(len(rows[row_value])): 
            letter = rows[row_value][letter_value]
            if letter == "A": 
                if check_left_diagnol(rows, row_value, letter_value) and check_right_diagnol(rows, row_value, letter_value): 
                    count += 1        
    print(count)


if __name__ == "__main__": 
    with open('input.txt', 'r') as inputText: 
        test_input = inputText.read()

    input_dict = []

    for i in test_input.split('\n'): 
        input_dict.append(i)

    check_X_MAS(input_dict)