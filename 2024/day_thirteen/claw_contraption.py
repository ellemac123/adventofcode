"""
https://adventofcode.com/2024/day/13
"""


TOKENS = {
    'A': 3, 
    'B': 1
}

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
    with open('tiny_input.txt', 'r') as f: 
        for i in f.readlines(): 
            if i.strip():
                directions.append(i.strip())

    formatted_directions = format_input(directions)
    print(formatted_directions)


if __name__ == "__main__": 
    run()