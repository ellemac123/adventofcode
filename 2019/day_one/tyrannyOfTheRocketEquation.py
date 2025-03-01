"""
Day one advent of code in python - https://adventofcode.com/2019/day/1

the answer for part one is: 3311492
"""
import math 

def find_mass(inputlist):
    """
    Given a list of numbers, calculate the fuel required by 
    dividing its value by three, rounding down, and 
    then subtracting 2
    """
    total = 0

    for i in inputlist: 
        total += (math.floor(i/3) - 2)

    return total

if __name__ == "__main__": 
    file_input = []
    with open('input.txt', 'r') as inputFile: 
        file_input = [int(line.strip()) for line in inputFile]

    total_mass = find_mass(file_input)

    print(f"the answer for part one is: {total_mass}")