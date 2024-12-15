"""
"Our computers are having issues, so I have no idea if we have any Chief Historians in stock! You're welcome to check the warehouse, though," says the mildly flustered shopkeeper at the North Pole Toboggan Rental Shop. The Historians head out to take a look.
The shopkeeper turns to you. "Any chance you can see why our computers are having issues again?"
The computer appears to be trying to run a program, but its memory (your puzzle input) is corrupted. All of the instructions have been jumbled up!

It seems like the goal of the program is just to multiply some numbers. It does that with instructions like mul(X,Y), where X and Y are each 1-3 digit numbers. For instance, mul(44,46) multiplies 44 by 46 to get a result of 2024. Similarly, mul(123,4) would multiply 123 by 4.

However, because the program's memory has been corrupted, there are also many invalid characters that should be ignored, even if they look like part of a mul instruction. Sequences like mul(4*, mul(6,9!, ?(12,34), or mul ( 2 , 4 ) do nothing.
Scan the corrupted memory for uncorrupted mul instructions. What do you get if you add up all of the results of the multiplications?

Your puzzle answer was `191183308` 
"""

import re

def regex_finder(input):
    regex = r'mul\(\d+\,\d+\)'
    found_results = re.findall(regex, input)
    return found_results
    
def sum_of_multipliers(input): 
    values = 0
    for i in input: 
        items = i.strip('mul(').strip(')').split(',')
        values = values + (int(items[0]) * int(items[1]))

    return values

if __name__ == "__main__": 
    with open('input.txt', 'r') as inputText: 
        test_input = inputText.read()

    regex_results = regex_finder(str(test_input))
    sum = sum_of_multipliers(regex_results)

    print(sum)
