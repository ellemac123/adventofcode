"""
As the search for the Chief continues, a small Elf who lives on the station tugs on your shirt; she'd like to know if you could help her with her word search (your puzzle input). She only has to find one word: XMAS.

This word search allows words to be horizontal, vertical, diagonal, written backwards, or even overlapping other words. It's a little unusual, though, as you don't merely need to find one instance of XMAS - you need to find all of them. Here are a few ways XMAS might appear, where irrelevant characters have been replaced with .:
"""
import re

MATCH = "XMAS"
MATCH2 = "SAMX"


def check_if_match(up_values): 
    if up_values == MATCH or up_values == MATCH2:
        return True
    else: 
        return False


def check_up(rows, current_row, current_position): 
    up_values = rows[current_row][current_position]

    for i in range(1, 4):
        if current_row - i < 0: 
            return False
        
        up_values = up_values + rows[current_row - i][current_position]
    
    return check_if_match(up_values)



def check_down(rows, current_row, current_position): 
    #check 4 down if they match MATCH
    up_values = rows[current_row][current_position]

    try: 
        for i in range(1, 4):
            up_values = up_values + rows[current_row + i][current_position]
        
        return check_if_match(up_values)
    except: 
        return False


def check_right(rows, current_row, current_position): 
    #check 4 right if they match MATCH
    try: 
        up_values = rows[current_row][current_position]
        for i in range(1, 4):
            up_values = up_values + rows[current_row][current_position + i]
        
        return check_if_match(up_values)
    except IndexError: 
        return False

def check_left(rows, current_row, current_position): 
    #check 4 left if they match MATCH
    up_values = rows[current_row][current_position]
    for i in range(1, 4):
        if current_position - i < 0: 
            return False
        up_values = up_values + rows[current_row][current_position - i]
    
    return check_if_match(up_values)

def check_up_right_diagnol(rows, current_row, current_position): 
    #check 4 left if they match MATCH
    try: 
        up_values = rows[current_row][current_position]
        for i in range(1, 4):
            if current_row - i < 0: 
                return False
            
            up_values = up_values + rows[current_row - i][current_position + i]
        
        return check_if_match(up_values)
    except IndexError: 
        return False

def check_up_left_diagnol(rows, current_row, current_position): 
    up_values = rows[current_row][current_position]

    for i in range(1, 4):
        if current_row - i < 0 or current_position - i < 0: 
            return False
        up_values = up_values + rows[current_row - i][current_position - i]
    return check_if_match(up_values)

def check_down_right_diagnol(rows, current_row, current_position): 
    #check 4 left if they match MATCH
    try: 
        up_values = rows[current_row][current_position]
        for i in range(1, 4):
            up_values = up_values + rows[current_row + i][current_position + i]
        
        return check_if_match(up_values)
    except IndexError: 
        return False

def check_down_left_diagnol(rows, current_row, current_position): 
    #check 4 left if they match MATCH
    try: 
        up_values = rows[current_row][current_position]
        for i in range(1, 4):
            if current_position - i < 0: 
                return False

            up_values = up_values + rows[current_row + i][current_position - i]
        
        return check_if_match(up_values)
    
    except IndexError: 
        return False


def check_X(rows): 
    count = 0
    for row_value in range(len(rows)): 
        for letter_value in range(len(rows[row_value])): 
            letter = rows[row_value][letter_value]
            if letter == "X": 
                if check_up(rows, row_value, letter_value): count += 1
                
                if check_down(rows, row_value, letter_value): count += 1

                if check_left(rows, row_value, letter_value): count += 1
                
                if check_right(rows, row_value, letter_value): count += 1

                if check_up_right_diagnol(rows, row_value, letter_value): count += 1

                if check_down_right_diagnol(rows, row_value, letter_value): count += 1

                if check_up_left_diagnol(rows, row_value, letter_value): count += 1

                if check_down_left_diagnol(rows, row_value, letter_value): count += 1
        
    print(count)


if __name__ == "__main__": 
    with open('input.txt', 'r') as inputText: 
        test_input = inputText.read()

    input_dict = []

    for i in test_input.split('\n'): 
        input_dict.append(i)

    check_X(input_dict)