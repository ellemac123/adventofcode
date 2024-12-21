

def setup_game_dictionary(line_input):
    print(line_input) 


if __name__ == "__main__": 
    with open('input.txt', 'r') as input: 
        input_data = input.read().splitlines()

    data_structure = setup_game_dictionary(input_data)