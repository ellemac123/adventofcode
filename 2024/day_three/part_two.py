"""
As you scan through the corrupted memory, you notice that some of the conditional statements are also still intact. If you handle some of the uncorrupted conditional statements in the program, you might be able to get an even more accurate result.

There are two new instructions you'll need to handle:

The do() instruction enables future mul instructions.
The don't() instruction disables future mul instructions.
Only the most recent do() or don't() instruction applies. At the beginning of the program, mul instructions are enabled.
"""

import re

def regex_finder(input):
    """
    Find all multipliers by using regex match on all of them
    """
    regex = r'mul\(\d+\,\d+\)'
    found_results = re.findall(regex, input)
    return found_results
    
def sum_of_multipliers(input): 
    """
        sum up all the multiplication inputs
    """
    values = 0
    for i in input: 
        items = i.strip('mul(').strip(')').split(',')
        values = values + (int(items[0]) * int(items[1]))

    return values

def find_dos(input): 
    """
        Split the srtring by "do()" and return all the strings 
        after "do()" since there might be multiple just return 
        all the lists after the first do()
    """
    a = []
    if "do()" in input: 
        a = input.split("do()")

    return a[1:]

def find_donts(input): 
    """
    Split the string by "don't()" command since we want to ignore these

    take the first one becuase it doesnt start with don't()
    """
    a = input.split("don't()")

    doList = []

    if not input.startswith("don't()"): 
        # only add the first one if it doesnt start with don't
        # this isnt actually handled in the loop but.. 
        doList.append(a[0])

    for i in a[1:]: 
        dos = find_dos(i)            
        doList.extend(dos)

    regexed = []
    for i in doList: 
        regexed.extend(regex_finder(i))

    return regexed
    

if __name__ == "__main__": 
    with open('input.txt', 'r') as inputText: 
        test_input = inputText.read()


    regexed_results = find_donts(test_input)
    sum = sum_of_multipliers(regexed_results)

    print(sum)
