"""
https://adventofcode.com/2024/day/14

"""
import math

def check_quads(final_locations, row, col): 
    quadrants = [
        # (row 0, row end), (col start, col end)
        [(0, math.ceil(row/2)), (0, math.ceil(col/2))], #q1
        [(0, math.ceil(row/2)),  math.ceil(col/2), col], #q1
        [(math.ceil(row/2), row), math.ceil(col/2), col], #q3
        [(math.ceil(row/2), row), (0, math.ceil(col/2))], # q4
    ]

    for quad in quadrants: 
        print(quad)


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
    formatted_input = [] 
    for a in file_input: 
        i = a.split(' ')
        starting_pos = [int(b) for b in i[0].replace('p=', '').strip().split(',')]
        velocity = [int(c) for c in i[1].replace('v=', '').strip().split(',')]

        formatted_input.append([starting_pos, velocity])
    
    return formatted_input

def run():
    file_input = [] 
    # space_x = 101
    # space_y = 103

    space_x = 11
    space_y = 7
    seconds = 100

    with open('tiny_input.txt', 'r') as f: 
        for a in f.readlines(): 
            file_input.append(a.strip())

    formatted_input = format_input(file_input)
    final_locations = safe_area(formatted_input, seconds, (space_x, space_y))
    
    check_quads(final_locations, col=space_x, row=space_y)
    

if __name__ == "__main__": 
    run()