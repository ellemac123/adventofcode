"""
https://adventofcode.com/2020/day/1

Solution for part one:  319531
Solution for part two:  244300320
"""

def sum(input_list):
    """
        For item in input list,
        subtract by 2020, abs value it, and see if its in the list

        if so return sum of the two values
    """
    for val in input_list:
        searcher = 2020 - val
        if searcher in input_list:
            return searcher * val

def triple_sum(input_list):
    """
    Loop through a

    Loop through b

    if 2020 - b - a in list
        return the product of a b and c
        else return -1
    """
    for a in input_list:
        sub = 2020 - a
        for b in input_list:
            c = sub - b
            if c in input_list:
                return c * a * b
    return -1

if __name__ == "__main__":
    input = []
    with open('input.txt', 'r') as f:
        for line in f:
            input.append(int(line))

    print('Solution for part one: ', sum(input))
    print('Solution for part two: ', triple_sum(input))

