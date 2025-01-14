"""
https://adventofcode.com/2024/day/11

Part One:
How many stones will you have after blinking 25 times?
Solution for Part One:  231278
"""


def format_input_string(input_string):
    """
    Given an input_string from the file,

    return it stripped, split, and turned into integers.
    """
    return [int(num) for num in input_string.strip().split(' ')]


def blink(stones):
    """
    If the stone is engraved with the number 0,
        it is replaced by a stone engraved with the number 1.
    If the stone is engraved with a number that has an even number of digits,
        it is replaced by two stones.
        The left half of the digits are engraved on the new left stone,
        and the right half of the digits are engraved on the new right stone.
        (The new numbers don't keep extra leading zeroes:
            1000 would become stones 10 and 0.)
    If none of the other rules apply,
        the stone is replaced by a new stone;
        the old stone's number multiplied by 2024 is engraved on the new stone.
    """
    plutonian_stones = []

    for stone in stones:
        char_stone = str(stone)
        if stone == 0:
            plutonian_stones.append(1)
        elif (len(char_stone) % 2 == 0):
            first_split = char_stone[:int(len(char_stone)/2)]
            second_split = char_stone[int(len(char_stone)/2):]

            # convert to int so you dont keep leading zeros
            plutonian_stones.append(int(first_split))
            plutonian_stones.append(int(second_split))
        else:
            multiplier = stone * 2024
            plutonian_stones.append(multiplier)

    return plutonian_stones

def run(input_list, blinks):
    """
    Given a list of blinks, transform the input_list that many times
    """
    morphed = input_list
    for i in range(blinks):
        morphed = blink(morphed)

    return len(morphed)

if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        input_text = f.read()

    input_list = format_input_string(input_text)
    blinks = 25

    print('Solution for Part One: ', run(input_list, blinks))