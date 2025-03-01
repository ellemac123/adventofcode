"""
Day one advent of code in python - https://adventofcode.com/2019/day/1

the answer for part one is: 3311492
the answer for part two is: 4964376
"""
import math 

def find_mass(inputlist):
    """
    Given a list of numbers, calculate the fuel required by 
    dividing its value by three, rounding down, and 
    then subtracting 2
    """
    total = 0
    part_two_total = 0

    for i in inputlist: 
        value = (math.floor(i/3) - 2)
        total += value

        while value > 0: 
            part_two_total += value
            value = (math.floor(value/3) - 2)

    return total, part_two_total

if __name__ == "__main__": 
    file_input = []
    with open('input.txt', 'r') as inputFile: 
        file_input = [int(line.strip()) for line in inputFile]

    total_mass, part_two_total_mass = find_mass(file_input)

    print(f"the answer for part one is: {total_mass}")
    print(f"the answer for part two is: {part_two_total_mass}")