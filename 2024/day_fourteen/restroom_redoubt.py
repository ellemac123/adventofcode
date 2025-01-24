"""
https://adventofcode.com/2024/day/14

The answer for part one is:  223020000
"""
import math
from collections import defaultdict

def mult_quads(quads_count): 
    total = 0
    for i in quads_count:
        if not total:
            total = quads_count[i]
        else: 
            total *= quads_count[i]

    return total


def check_quads(final_locations, row, col): 
    final_count = defaultdict(int)
    quadrants = [
        # (row 0, row end), (col start, col end)
        [(0, math.floor(row/2)), (0, math.floor(col/2))], #q1
        [(0, math.floor(row/2)),  (math.ceil(col/2), col)], #q2
        [(math.ceil(row/2), row), (0, math.floor(col/2))], # q3
        [(math.ceil(row/2), row), (math.ceil(col/2), col)], #q3
    ]

    for xi in final_locations: 
        x = xi[0]
        y = xi[1]

        for num, a in enumerate(quadrants): 
            if x in range(a[0][0], a[0][1]): 
                if y in range(a[1][0], a[1][1]): 
                    final_count[num+1] += 1
    
    return final_count
            

def safe_area(formatted_input, seconds, board): 
    finals = []
    for _, val in enumerate(formatted_input): 
        col = val[0][0]
        row = val[0][1]

        vel_col = val[1][0] * seconds
        vel_row = val[1][1] * seconds

        final_col = (col + vel_col)
        final_row = (row + vel_row)
        finals.append([final_row%board[1], final_col%board[0]])

    return finals

def format_input(file_input):
    """
    Given the raw file input, make it useful for our puzzle and return
    """
    formatted_input = [] 
    for a in file_input: 
        i = a.split(' ')
        starting_pos = [int(b) for b in i[0].replace('p=', '').strip().split(',')]
        velocity = [int(c) for c in i[1].replace('v=', '').strip().split(',')]

        formatted_input.append([starting_pos, velocity])
    
    return formatted_input

def run():
    file_input = [] 
    space_x = 101
    space_y = 103
    seconds = 100

    with open('input.txt', 'r') as f: 
        for a in f.readlines(): 
            file_input.append(a.strip())

    formatted_input = format_input(file_input)
    final_locations = safe_area(formatted_input, seconds, (space_x, space_y))
    
    quads_count = check_quads(final_locations, col=space_x, row=space_y)
    total = mult_quads(quads_count)

    print('The answer for part one is: ', total)

if __name__ == "__main__": 
    run()