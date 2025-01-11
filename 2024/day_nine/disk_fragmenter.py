"""
https://adventofcode.com/2024/day/9

part one solution:

2333133121414131402
"""
def convert_to_list(file_line):
    """
    Convert the list into the files and free space indicator
    required and return this
    """
    conversion_string = []
    id = 0
    i = 0
    stop = len(file_line)
    while i < stop:
        for a in range(int(file_line[i])):
            conversion_string.append(id)
        if i+1 < stop:
            for b in range(int(file_line[i + 1])):
                conversion_string.append('.')
        id = id + 1
        i += 2

    return conversion_string

if __name__ == "__main__":
    with open('tiny_input.txt', 'r') as input_file:
        line = input_file.readline()

    convert_to_list(list(line))