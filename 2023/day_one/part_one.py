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