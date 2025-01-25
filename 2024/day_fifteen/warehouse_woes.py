"""
https://adventofcode.com/2024/day/15

The answer for part one is:  1436690
"""

DIRECTIONS = {
    '^': (-1, 0), 
    '>': (0, 1), 
    'v': (1, 0), 
    '<': (0, -1),
}


def find_starting_position(input_map, value='@'): 
    """
    Given a list and a value to find
        return the row, col of the value we are searching for
    """
    for row_num, row in enumerate(input_map): 
        if value in row: 
            return (row_num, row.index(value))


def move_piece(input_map, coords, direction): 
    """
    Recursive function - 
    if the next coord in given direction is '.', move current piece to this spot
    or break if you find a '#' sign

    if you find the # sign
        find the coord 1 to the oppositie direction of the # sign and update '.'
        continue to do this until you reach the @ sign  
        place a '.' there 
    else 
        do nothing
    """
    check_row = direction[0] + coords[0]
    check_val = direction[1] + coords[1]
    spot_check = input_map[check_row][check_val]
    if spot_check == '#':
        return input_map
    elif spot_check == '.':
        input_map[check_row][check_val] = input_map[coords[0]][coords[1]]
        input_map[coords[0]][coords[1]] = '.'
        return input_map
    else: 
        input_map = move_piece(input_map, (check_row, check_val), direction) 
        if input_map[check_row][check_val] == '.': 
            input_map[check_row][check_val] = input_map[coords[0]][coords[1]]
            input_map[coords[0]][coords[1]] = '.'
        return input_map          


def move(input_map, coords, coordinates_order):
    """
    Given an input_map, starting poisiotn of the @ sign, and 
    the list of coordinates

    Loop through the movements
        for each movement get the corresponding direction

        loop through and find the first coord in that direction that is '.'
        or break if you find a '#' sign

        if you find the # sign
            find the coord 1 to the oppositie direction of the # sign and update '.'
            continue to do this until you reach the @ sign  
            place a '.' there 
        else 
            do nothing
    """
    for movement in coordinates_order: 
        # Loop through the movements - for each movement get the corresponding direction
        direction = DIRECTIONS[movement]    
        input_map = move_piece(input_map, coords, direction)
        coords = find_starting_position(input_map)

    return input_map


def calculate_box_positions(final_map, box='O'): 
    total = 0
    for ri, row in enumerate(final_map): 
        for ci, col in enumerate(row): 
            if col == box: 
                total += ((100 * ri) + ci)
    return total


def run(input_map, coordinates_row): 
    starting_position = find_starting_position(input_map)

    final_map = move(input_map, starting_position, coordinates_row)
    total_sum = calculate_box_positions(final_map=final_map)

    return total_sum


if __name__ == "__main__": 
    """
    Format the input and run the application code!
    Print the answer for part one
    """
    input_map = []
    temp_coords = []
    coords = []
    with open('input.txt', 'r') as f: 
        lines = f.readlines()
        for iterr, a in enumerate(lines): 
            if a == '\n': 
                temp_coords = list(lines[iterr+1:])
                break
            else: 
                input_map.append(list(a.strip()))
    

    for i in temp_coords: 
        coords.extend(list(i.strip()))

    result = run(input_map, coords)
    print('The answer for part one is: ', result)