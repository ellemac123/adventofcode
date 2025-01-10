from csv import DictReader
OPERATORS = [
    '-', 
    '+', 
    '/', 
    '*'
]

def create_shape(input_file): 
    new_list = []
    for line in input_file: 
        split = line.strip().split(':')
        total = split[0]
        numerics = split[1].strip().split(' ')
        new_list.append((total, numerics))

    return new_list

if __name__ == "__main__": 
    file_input = []
    with open('tiny_input.txt', 'r') as file: 
        for line in file.readlines(): 
            file_input.append(line.strip())

    shaped_list = create_shape(file_input)
    print(shaped_list)