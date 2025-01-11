"""
https://adventofcode.com/2024/day/9

solution for tiny_input.txt part one: 1928
solution for part one: 6259790630969

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
        if '.' not in space_copy:
            new_list.extend([int(n) for n in space_copy])
            break
        elif space_indicator_list[i] == '.':
            dots = dots + 1
            string = ''.join(space_copy).rstrip('.')
            space_copy = list(string)[1:-1]

            if string:
                new_list.append(int(string[-1]))

        else:
            space_copy = space_copy[1:]
            new_list.append(int(space_indicator_list[i]))

    return new_list

def product_time(final_list):
    """
    Calculate the sum of all the products of position
    and number at that position
    """
    total = 0
    for v, num in enumerate(final_list):
        if num != '.':
            total += v * num

    return total



if __name__ == "__main__":
    with open('tiny_input.txt', 'r') as input_file:
        line = input_file.readline()

    converted_list = convert_to_list(list(line))
    space_list = move_file_blocks(converted_list)
    total_sum = product_time(space_list)
    print('solution for part one:', total_sum)
