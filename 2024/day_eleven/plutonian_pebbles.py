"""
https://adventofcode.com/2024/day/11

Part One:
How many stones will you have after blinking 25 times?

Solution for Part One:  231278
initial solution = time =  0:00:00.263549
tiny input = time =  0:00:00.066682
Using a Dict over a list:
    Speed:  0:00:00.002515

Part Two:
How many stones will you have after blinking 75 times?

Part Two with speed improvement:  274229228071551
    Speed: 0:00:00.112909
"""
import datetime
from collections import Counter, defaultdict


def format_input_string(input_string):
    """
    Given an input_string from the file,
    return it stripped, split, and turned into integers.
    """
    return [int(num) for num in input_string.strip().split(' ')]

def run(input_list, blinks):
    """
    This was a crazy one - originally used a loop with a list, but it
    grew exponentially so have swapped to a dict since order isn't important here
    """
    input_list = Counter(input_list)
    for n in range(blinks):
        iteration_stone = defaultdict(int)
        for stone in input_list.keys():
            val = input_list[stone]
            if stone == 0:
                iteration_stone[1] += val
            else:
                char_stone = len(str(stone))
                if char_stone % 2 == 0:
                    # halfway = 10 to the power of floor divided digits
                    halfway = 10 ** (char_stone // 2)
                    right = stone // halfway
                    left = stone % halfway

                    iteration_stone[right] += val
                    iteration_stone[left] += val
                else:
                    iteration_stone[stone * 2024] += val

        input_list = iteration_stone

    sum = 0
    for a in input_list.keys():
        sum = sum + input_list[a]
    return sum



if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        input_text = f.read()

    input_list = format_input_string(input_text)
    blinks = 25
    tim = datetime.datetime.now()
    print('Part One: ', run(input_list, blinks))
    tim2 = datetime.datetime.now()
    print('Part One Time: ', tim2 - tim)

    blinks = 75
    tim = datetime.datetime.now()
    print('\nPart Two: ', run(input_list, blinks))
    tim2 = datetime.datetime.now()
    print('Part Two Time: ', tim2 - tim)
