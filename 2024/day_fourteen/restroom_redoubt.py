"""
https://adventofcode.com/2024/day/14

"""

def run():
    file_input = [] 
    with open('tiny_input.txt', 'r') as f: 
        for a in f.readlines(): 
            file_input.append(a.strip())

    print(file_input)

if __name__ == "__main__": 
    run()