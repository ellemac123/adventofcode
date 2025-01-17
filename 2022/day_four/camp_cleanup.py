"""
https://adventofcode.com/2022/day/4

solution for part one:  424
solution for part two:  804
"""
def setup_pairs(input_list): 

    count = 0
    part_two_count = 0
    for line in input_list: 
        first_elf = line[0].split('-')
        second_elf = line[1].split('-')

        first = set(a for a in range(int(first_elf[0]), int(first_elf[1])+ 1))
        second = set(b for b in range(int(second_elf[0]), int(second_elf[1])+ 1))

        if first.issubset(second) or second.issubset(first):
            count += 1

        if any({a}.issubset(second) for a in first) or any({b}.issubset(first) for b in second):
            part_two_count += 1

    
    return count, part_two_count


if __name__ == "__main__": 
    input = []
    with open('input.txt', 'r') as f: 
        for a in f.readlines(): 
            in_line = a.split(',')
            input.append([in_line[0].strip(), in_line[1].strip()])
    
    answer_one, answer_two = setup_pairs(input)
    print('solution for part one: ', answer_one)
    print('solution for part two: ', answer_two)