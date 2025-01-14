"""
https://adventofcode.com/2020/day/2

Valid Policies for Part One:  640

"""
from collections import Counter

def format_input(input_list):
    """
    Given a list,
    return a list containing a tuple and a string
    """
    formatter = []
    for item in input_list:
        split = item.split(' ')
        pw = split[0].strip().split('-')
        formatter.append([int(pw[0]),
                         int(pw[1]),
                         split[1].replace(':', '').strip(),
                         split[2]])

    return formatter

def run(formatted_input):
    """
    Loop through and return valid policies

    Each line gives the password policy [0], [1], [2] and then the password[3].
    The password policy indicates the lowest [0] and highest [1] number of times a
        given letter [2] must appear for the password [3] to be valid.
    """
    sum = 0
    for line in formatted_input:
        char_one = line[0]
        char_two = line[1]
        polly = line[2]
        password = Counter(list(line[3]))
        if char_one <= password[polly] <= char_two:
            sum = sum + 1
    return sum


if __name__ == "__main__":
    input_file = []
    with open('input.txt', 'r') as f:
        for line in f:
            input_file.append(line.strip())

    formatted_input = format_input(input_file)
    print('Valid Policies for Part One: ', run(formatted_input))
