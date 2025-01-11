"""
https://adventofcode.com/2024/day/9

part one solution:

"""
import re
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
            for b in range(int(file_line[i + 1])):
                conversion_string.append('.')
        id = id + 1
        i += 2
    print(conversion_string)
    return conversion_string

def move_file_blocks(space_indicator_list):
    pattern = r'\.'
    ra = int(len(space_indicator_list) / 2) + 2
    print('here')
    for i in range(1, ra):
        # traversing backwards in the list
        # check if the number is a digit
        # if not, continue on
        if space_indicator_list[-i].isdigit():
            stringed = ''.join(space_indicator_list)
            match = re.search(pattern, stringed)
            try:
                loc = match.start()
            except:
                break
            val = space_indicator_list[-i]


            space_indicator_list[loc] = val
            space_indicator_list[-i] = 'X'

    return space_indicator_list

def product_time(final_list):
    biggy = []
    for i in final_list:
        if i.isdigit():
            biggy.append(i)

    prods = []
    for v in range(len(biggy)):
        f = v * int(biggy[v])
        prods.append(f)

    return sum(prods)



if __name__ == "__main__":
    with open('input.txt', 'r') as input_file:
        line = input_file.readline()

    converted_list = convert_to_list(list(line))
    space_list = move_file_blocks(converted_list)
    print(product_time(space_list))
