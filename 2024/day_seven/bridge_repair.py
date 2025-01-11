"""
https://adventofcode.com/2024/day/7

solution for part 1:  303766880536
"""

from itertools import product

def create_shape(input_file):
    new_list = []
    for line in input_file: 
        split = line.strip().split(':')
        total = split[0]
        numerics = split[1].strip().split(' ')
        new_list.append((total, numerics))

    return new_list

def multiply(number_one, number_two): 
    return number_one * number_two

def evaluate_string(total, values_array): 
    flag = True    
    i = 0 
    while flag: 
        if len(values_array) >= 3: 
            if not values_array[i + 1].isdigit(): 
                if values_array[i + 1] == '+': 
                    values_array[i] = sum([values_array[i], values_array[i+2]])
                elif values_array[i + 1] == '|':
                    digit = str(values_array[i]) + str(values_array[i + 2])
                    values_array[i] = int(digit)
                else:
                    values_array[i] = multiply(values_array[i], values_array[i+2])
                
                values_array.pop(i+2)
                values_array.pop(i+1)
        else: 
            flag = False

    if values_array[0] == total: 
        return True
    return False

def run(shaped_data, part_two=False):
    """
    Given a list, call check_match to see if there is a way to
    create the total from the list

    if so add to count, sum and return
    """
    totals = []

    for i in shaped_data:
        sum_ = int(i[0])
        values = [int(num) for num in i[1]]

        if part_two:
            combos = (list(product('+|*', repeat=len(values) - 1)))
        else:
            combos = (list(product('+*', repeat=len(values) - 1)))

        for iter in range(len(combos)):
            """loop through all the combos"""
            final = []
            operator_string = combos[iter]
            # order values
            for i in range(len(values)):
                final.append(values[i])
                if i < len(operator_string): 
                    final.append(operator_string[i])

            if evaluate_string(sum_, final): 
                totals.append(sum_)
                break

    return sum(totals)



if __name__ == "__main__": 
    file_input = []
    with open('input.txt', 'r') as file:
        for line in file.readlines(): 
            file_input.append(line.strip())

    shaped_list = create_shape(file_input)
    totals = run(shaped_list)

    print('solution for part 1: ', totals)
    print('solution for part 2: ', run(shaped_list, part_two=True))