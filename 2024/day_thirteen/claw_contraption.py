"""
https://adventofcode.com/2024/day/13

The solution for part one is:  31897
time elapsed with generator:  0:00:05.222259
switching to a math equation: time elapsed:  0:00:00.028963
jeez!
"""
import datetime
import math
import numpy as np

def format_input(input_list): 
    """
    format the inputs so we can work with a list of lists

    the list will contain: 
        [A button x,y values, B button x,y values, Prize X and Prize Y values]
    """
    formatted_directions = []
    for i in np.arange(0, len(input_list),3): 
        first = [int(a.split('+')[1]) for a in input_list[i].split(': ')[1].split(', ')]
        second = [int(b.split('+')[1]) for b in input_list[i+1].split(': ')[1].split(', ')]
        third = [int(c.split('=')[1]) for c in input_list[i+2].split(': ')[1].split(', ')]
        
        formatted_directions.append([first, second, third])

    return formatted_directions

def do_math(prize, a_buttons, b_buttons, BIG_NUMBER, i): 
    b = ((prize[0] + BIG_NUMBER) - (a_buttons[0] * i)) / b_buttons[0]
    if b < 0: 
        return b
    if b % 1 == 0:
        if (a_buttons[1] * i) +  (b_buttons[1] * b) == prize[1] + BIG_NUMBER: 
            t = (3 * i) + (b * 1)
            # print('a and b matches')
            return t
    
def combinations(formatted_directions, BIG_NUMBER = 0): 
    """
    Given two values, find the most amount of calls possible
    by splitting Prize/smaller of the two buttons

    the do math and if the calculations work, 
    add tokens to a dict, list
    """

    final_token_count = 0
    for combo in formatted_directions: 
        print(combinations)
        # print(combo)
        a_buttons = combo[0]
        b_buttons = combo[1]
        prize = combo[2]
        tokens = []
        max_value = np.min([a_buttons[0], b_buttons[0]])
        
        rg = math.ceil((prize[0]+BIG_NUMBER)/(max_value))

        for i in np.arange(rg): 
            b = do_math(prize, a_buttons, b_buttons, BIG_NUMBER, i)
            if b:
                if b < 0: 
                    continue
                else:
                    tokens.append(b)
        if tokens: 
            final_token_count += min(tokens)

    return final_token_count


def run(): 
    """
    format input
    run through code
    print solutions
    """
    directions = []
    with open('input.txt', 'r') as f: 
        for i in f.readlines(): 
            if i.strip():
                directions.append(i.strip())

    formatted_directions = format_input(directions)

    start = datetime.datetime.now()
    tokens = combinations(formatted_directions)    
    print('The solution for part one is: ', tokens)
    print('time elapsed: ', datetime.datetime.now() - start)

    BIG_NUMBER = 10000000000000
    print('The solution for part two is: ', combinations(formatted_directions, BIG_NUMBER))


if __name__ == "__main__": 
    run()