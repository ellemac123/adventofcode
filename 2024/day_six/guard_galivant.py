positions = {
    # row, col
    '^': (-1, 0), 
    '>': (0, 1), 
    'v': (1, 0),
    '<': (0, -1)
}

def count_traversals(final_list): 
    """
        Count up all the X's in the list 
        return the total count + 1 for the final resting spot of v
    """
    count = 0
    for i in final_list: 
        for j in i: 
            if j == 'X': 
                count+=1
    # add one to the count for the final v position
    return count +1

def find_v(input_list): 
    """
        Return starting position of guard as: row, position
    """
    for i in range(len(input_list)): 
        if '^' in input_list[i]:
            return i, input_list[i].index('^')

def progress_map(input_list, current_row, current_column): 
    """
        Progress through the map, leaving an X everywhere you 
        went
    """
    new_list = []
    for i in input_list: 
        new_list.append(list(i))
    
    while True:
    # get value in positions
        v_value = new_list[current_row][current_column]
        next_increment = positions[v_value]
    # check next position
        next_row = current_row + next_increment[0]
        next_column = current_column + next_increment[1]
        try:
            next_spot = new_list[next_row][next_column]

            if next_spot != '#': 
                # move there, set old spot to 'X'
                # set the current (traversed) row / column to "X"
                new_list[current_row][current_column] = 'X'

                # set the current to the next one
                current_row = next_row
                current_column = next_column
                
                # set the v_value to the spot
                new_list[current_row][current_column] = v_value
            elif next_spot == '#':
            # if # in the spot, turn position 
                if v_value == '^':
                    v_value = '>'
                elif v_value == '>':
                    v_value = 'v'
                elif v_value == 'v':
                    v_value = '<'
                elif v_value == '<':
                    v_value = '^'
                new_list[current_row][current_column] = v_value
        except: 
            # if hit space that dne, exit while
            break
    
    return new_list
    # count up all x's in the list and return 


if __name__ == "__main__": 
    with open('input.txt', 'r') as input_file: 
        file_input = input_file.read().splitlines()

    v_row, v_column = find_v(file_input)

    x_list = progress_map(file_input, v_row, v_column)

    print(count_traversals(x_list))