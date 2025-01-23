"""
https://adventofcode.com/2024/day/14

"""


def safe_area(quads, formatted_input, seconds, board): 
    print(quads)

    for _, val in enumerate(formatted_input): 
        col = val[0][0]
        row = val[0][1]

        vel_col = val[1][0] * seconds
        vel_row = val[1][1] * seconds

        final_col = (col + vel_col)
        final_row = (row + vel_row)

        if final_col/board[0] > 0 :
            final_col = col + (final_col%board[0])
        else: 
            final_col = col - (final_col%board[0])

        if final_row/board[1] > 0: 
            final_row = row + (final_row%board[1])
        else: 
            final_row = row - (final_row%board[1])


        print(final_row, final_col)


def calculate_quadrants(x, y): 
    return int(x/2), int(y/2)

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
    quads = calculate_quadrants(space_x, space_y)

    safe_area(quads, formatted_input, seconds, (space_x, space_y))
    
    

if __name__ == "__main__": 
    run()