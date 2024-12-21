"""
The newly-improved calibration document consists of lines of text; each line originally contained a specific calibration value that the Elves now need to recover. On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.

For example:

1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.

Consider your entire calibration document. What is the sum of all of the calibration values?

Your puzzle answer was 55538.
"""

import re

def sum_calibration(input_list): 
    return sum(input_list)

def get_digits(input): 
    digit_input = []
    regex = re.compile(r'\d')
    for i in input: 
        a = regex.findall(regex, i)
        if len(a) > 0: 
            digit_input.append(int("".join([a[0], a[-1]])))

    return sum_calibration(digit_input)
        
if __name__ == "__main__": 
    with open('input.txt', 'r') as input_file: 
        a = input_file.read().splitlines()

    digits = get_digits(a)
    
    print("Sum: ", digits)