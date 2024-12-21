"""
--- Part Two ---
Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters: one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".

Equipped with this new information, you now need to find the real first and last digit on each line. For example:

two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.

What is the sum of all of the calibration values?

Your puzzle answer was 54875.
"""
import re
from part_one import sum_calibration

digits = {
    'one': 1, 
    'two': 2, 
    'three': 3, 
    'four': 4, 
    'five': 5, 
    'six': 6, 
    'seven': 7, 
    'eight': 8, 
    'nine': 9, 
}

def mapping(input_list):
    """
    Given a list of strings that contain digits, letters, and digits as words
    convert this to a list of integers, take the first and last digit, combine them to 
    form one number
    then sum all of these combined numbers for a total that is returned
    """
    counter = 0
    for i in input_list: 
        lista = []
        for pos in range(len(i)): 
            if i[pos].isdigit(): 
                lista.append(i[pos])
            else: 
                for digit in digits: 
                    if i[pos:].startswith(digit):
                        lista.append(str(digits[digit]))
        if lista:
            counter = counter + int(lista[0] + lista[-1])
    
    return counter

if __name__ == "__main__": 
    with open('input.txt', 'r') as input_file: 
        a = input_file.read().splitlines()

    print(mapping(a))