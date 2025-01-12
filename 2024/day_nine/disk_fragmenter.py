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

def move_file_blocks(original_list):

    """
    Given a 'original' list, remove all the dots and put
    them in a new 'numbers' list

    create a finals empty list

    loop through the original list

    if value is digit
    append to final list
    pop first value in the numbers list

    if its a dot
    append numbers[-1] to finals list
    remove numbers[-1] from the numbers list

    end and return if the numbers list is empty
    """

    numbers_list = [i for i in original_list if i != '.']
    # create a 'finals' empty list
    final_list = []

    # loop through original loop
    for _, value in enumerate(original_list):
        # if value is a number
        # append [0] to finals list
        # remove [0] from the numbers list
        if numbers_list:
            if value.isdigit():
                final_list.append(int(numbers_list[0]))
                numbers_list.pop(0)
            else:
                final_list.append(int(numbers_list[-1]))
                numbers_list.pop()
        else:
            return final_list

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
    with open('input.txt', 'r') as input_file:
        line = input_file.readline()

    converted_list = convert_to_list(list(line))
    space_list = move_file_blocks(converted_list)
    total_sum = product_time(space_list)
    print('solution for part one:', total_sum)
