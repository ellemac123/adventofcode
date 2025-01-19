"""
https://adventofcode.com/2024/day/13

The solution for part one is:  31897
time elapsed with generator:  0:00:05.222259
"""

import math
import datetime 
from itertools import product

def combinations(formatted_directions): 
    """
        Given two values, find the most amount of calls possible
        by splitting Prize/smaller of the two buttons

        then calculate all the possible products
        sum them 
        add tokens to a dict, list
    """

    final_token_count = 0
    for combo in formatted_directions: 
        a_buttons = combo[0]
        b_buttons = combo[1]
        prize = combo[2]
        tokens = []
        max_value = min(a_buttons[0], b_buttons[0])

        for i in generate_cartesian(prize[0], max_value): 
            if (a_buttons[0] * i[0]) +  (b_buttons[0] * i[1]) == prize[0]: 
                if (a_buttons[1] * i[0]) +  (b_buttons[1] * i[1]) == prize[1]: 
                    t = (3 * i[0]) + (i[1]*1)
                    tokens.append(t)
    
        if tokens: 
            final_token_count += min(tokens)

    return final_token_count


def generate_cartesian(prize_value, max_value): 
    # prize_value += 10000000000000
    max_iterations = math.ceil(prize_value / max_value)

    for combo in product(range(1, max_iterations), repeat=2): 
        yield combo

def format_input(input_list): 
    """
    format the inputs so we can work with a list of lists

    the list will contain: 
        [A button x,y values, B button x,y values, Prize X and Prize Y values]
    """
    formatted_directions = []
    for i in range(0, len(input_list),3): 
        first = [int(a.split('+')[1]) for a in input_list[i].split(': ')[1].split(', ')]
        second = [int(b.split('+')[1]) for b in input_list[i+1].split(': ')[1].split(', ')]
        third = [int(c.split('=')[1]) for c in input_list[i+2].split(': ')[1].split(', ')]
        
        formatted_directions.append([first, second, third])

    return formatted_directions


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

if __name__ == "__main__": 
    run()