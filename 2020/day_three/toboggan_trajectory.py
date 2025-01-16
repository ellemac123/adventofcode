"""
https://adventofcode.com/2020/day/3
"""
TREE = '#'

def traverse(input_file, traversal):
    """
    while true
    traverse through the list by increasing the traversal
    when you go out of bounds break out
    """
    trees_encountered = 0
    pos = [0, 0]
    while pos[0] < len(input_file) and pos[1] < len(input_file[0]):
        print(pos[0], pos[1])
        if input_file[pos[0]][pos[1]] == TREE:
            print('tree found')
            trees_encountered = trees_encountered +  1
        pos[0] = pos[0] + traversal[0]
        pos[1] = pos[1] + traversal[1]

    return trees_encountered




if __name__ == "__main__":
    input_file = []
    with open('input.txt', 'r') as f:
        for a in f.readlines():
            input_file.append(a.strip())

    traversal = (3, 1)

    trees_encountered = traverse(input_file, traversal)
    print(trees_encountered)