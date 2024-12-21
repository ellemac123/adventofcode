colour_rules = {
    'red': 12, 
    'green': 13, 
    'blue': 14
}

def sum_data(input_data):
    """
    Sum up the ints in a given list of ints
    """
    return sum(input_data)

def setup_game_dictionary(line_input):
    """
        Setup the game dictionary based on the input 
    """
    game_dict = {}
    for i in range(len(line_input)): 

        a = line_input[i].split(':')[1].strip().split(';')
        rolls = []
        for line in a: 
            roll = dict()
            for j in line.strip().split(','): 
                colour = j.strip().split(' ')
                roll[colour[1].strip()] = colour[0].strip()

            rolls.append(roll)
        game_dict[i] = rolls
    return game_dict


def find_matches(game_dict): 
    """
        Run through the game dictionary, if each game in each dictionary matches
        add the game id to the matches list

        return matches  
    """
    matches = []
    for i in game_dict: 
        flag = True
        for game in game_dict[i]: 
            for colour in colour_rules: 
                if colour in game.keys(): 
                    if int(game[colour]) > colour_rules[colour]: 
                        flag = False
        if flag: 
            matches.append(i+1)
    return matches



if __name__ == "__main__": 
    with open('input.txt', 'r') as input: 
        input_data = input.read().splitlines()

    game_data_structure = setup_game_dictionary(input_data)
    matches = find_matches(game_data_structure)
    print(sum_data(matches))
