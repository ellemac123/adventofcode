DIRECTIONS = {
    '^': (-1, 0), 
    '>': (0, 1), 
    'v': (1, 0), 
    '<': (0, -1),
}

def run(input_map, coordinates_row): 
    print(input_map)
    print(coordinates_row)


if __name__ == "__main__": 
    input_map = []
    coords = []
    with open('tiny_input.txt', 'r') as f: 
        lines = f.readlines()
        for iterr, a in enumerate(lines): 
            if a == '\n': 
                coords = list(lines[iterr+1])
                break
            else: 
                input_map.append(list(a.strip()))
    
    run(input_map, coords)