"""
https://adventofcode.com/2024/day/9

solution for tiny_input.txt part one: 1928
solution for part one: 6259790630969

"""
from collections import Counter


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
            total += v * int(num)

    return total


def move_part_two(original_numbers):
    """
    given an original list of numerics
    create a list of just the numbers
    create a dict of the numbers and their count

    create a list of "final" numbers

    loop through the "numbers list"
    get the count for the number and the first index of it

    look in the original list between the start and it's index

    if there is a spaceof dots >= to the numbers count



    """
    numbers = sorted(set([int(i) for i in original_numbers if i != '.']), reverse=True)
    numbers = [str(i) for i in numbers]
    finals = original_numbers.copy()
    print(finals)
    print(numbers)
    counter = Counter(original_numbers)
    # loop through "numbers" time
    for numb in numbers:
        length_number = counter[numb]

        try:
            first_spot = finals.index(str(numb))
        except ValueError:
            import pdb; pdb.set_trace()
        joined_final_string = ''.join(finals)

        create_substring = '.' * length_number
        try:
            index_of_substring = joined_final_string[:first_spot].index(create_substring)
            if index_of_substring != -1 and index_of_substring < first_spot:
                moving = [str(numb)] * length_number
                finals[index_of_substring:index_of_substring + length_number] = list(moving)
                finals[first_spot:first_spot + length_number] = ['.'] * length_number
        except ValueError:
            pass

    return finals


if __name__ == "__main__":
    with open('input.txt', 'r') as input_file:
        line = input_file.readline()

    listed_line = list(line)

    converted_list = convert_to_list(listed_line)
    # space_list = move_file_blocks(converted_list)
    # total_sum = product_time(space_list)
    # print('solution for part one:', total_sum)


    part_two = move_part_two(converted_list)
    total_sum_two = product_time(part_two)
    print('solution for part two:', total_sum_two)

