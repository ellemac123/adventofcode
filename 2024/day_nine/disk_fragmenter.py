"""
https://adventofcode.com/2024/day/9

tiny_input solution: 1928
part one solution:

"""
def convert_to_list(file_line):
    """
    Convert the list into the files and free space indicator
    required and return this
    """
    conversion_string = []
    id = 0
    i = 0
    while i < len(file_line):
        for a in range(int(file_line[i])):
            conversion_string.append(str(id))
        if i+1 < len(file_line):
            conversion_string.extend(['.'] * int(file_line[i + 1]))
        id += 1
        i += 2
    return conversion_string

def move_file_blocks(space_indicator_list):
    dots = 1
    new_list = []
    space_copy = space_indicator_list.copy()
    for i in range(len(space_indicator_list)):
        if (dots + len(new_list)) == len(space_indicator_list):
            break
        elif space_indicator_list[i] == '.':
            dots = dots + 1
            string = ''.join(space_copy).rstrip('.')
            space_copy = list(string)[:-1]
            if string:
                new_list.append(int(string[-1]))
        else:
           new_list.append(int(space_indicator_list[i]))

    return new_list[:-1]

def product_time(final_list):
    """
    Calculate the sum of all the products of position
    and number at that position
    """
    total = 0
    for v, num in enumerate(final_list):
        total += v * num

    return total



if __name__ == "__main__":
    with open('tiny_input.txt', 'r') as input_file:
        line = input_file.readline()

    converted_list = convert_to_list(list(line))
    space_list = move_file_blocks(converted_list)
    print(product_time(space_list))
