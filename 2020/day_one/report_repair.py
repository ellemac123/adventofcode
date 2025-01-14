

def run(input_list):
    """
        For item in input list,
        subtract by 2020, abs value it, and see if its in the list

        if so return sum of the two values
    """
    for val in input_list:
        searcher = 2020 - val
        if searcher in input_list:
            return searcher * val

if __name__ == "__main__":
    input = []
    with open('input.txt', 'r') as f:
        for line in f:
            input.append(int(line))

    print('Solution for part one: ', run(input))
