"""
-- Day 2: Cube Conundrum ---
As you walk, the Elf shows you a small bag and some cubes which are either red, green, or blue. Each time you play this game, he will hide a secret number of cubes of each color in the bag, and your goal is to figure out information about the number of cubes.
To get information, once a bag has been loaded with cubes, the Elf will reach into the bag, grab a handful of random cubes, show them to you, and then put them back in the bag. He'll do this a few times per game.
You play several games and record the information from each game (your puzzle input). Each game is listed with its ID number (like the 11 in Game 11: ...) followed by a semicolon-separated list of subsets of cubes that were revealed from the bag (like 3 red, 5 green, 4 blue).
The Elf would first like to know which games would have been possible if the bag contained only 12 red cubes, 13 green cubes, and 14 blue cubes?
In the example above, games 1, 2, and 5 would have been possible if the bag had been loaded with that configuration. However, game 3 would have been impossible because at one point the Elf showed you 20 red cubes at once; similarly, game 4 would also have been impossible because the Elf showed you 15 blue cubes at once. If you add up the IDs of the games that would have been possible, you get 8.
Determine which games would have been possible if the bag had been loaded with only 12 red cubes, 13 green cubes, and 14 blue cubes. What is the sum of the IDs of those games?
Your puzzle answer was 2617.

--- Part Two ---
The Elf says they've stopped producing snow because they aren't getting any water! He isn't sure why the water stopped; however, he can show you how to get to the water source to check it out for yourself. It's just up ahead!
As you continue your walk, the Elf poses a second question: in each game you played, what is the fewest number of cubes of each color that could have been in the bag to make the game possible?
For each game, find the minimum set of cubes that must have been present. What is the sum of the power of these sets?
Your puzzle answer was 59795.
"""
import math
colour_rules = {
    'red': 12, 
    'green': 13, 
    'blue': 14
}

def power_data(input_data): 
    """
    given a list of dicts of game input, multiply each value in each row
    add that multiplied value to a list,
    return the list
    """
    power_list = []
    for i in input_data: 
        power_list.append(math.prod(i.values()))
    return power_list

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


def find_sum_matches(game_dict): 
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

def find_maxs_games(game_dict): 
    max_dict = []

    for i in game_dict: 
        max_list = dict()
        for game in game_dict[i]: 
            for colour in colour_rules: 
                if colour in game.keys(): 
                    if colour not in max_list.keys() or int(max_list[colour]) < int(game[colour]): 
                        max_list[colour] = int(game[colour])
        
        max_dict.append(max_list)

    return max_dict



if __name__ == "__main__": 
    with open('input.txt', 'r') as input: 
        input_data = input.read().splitlines()
    
    game_data_structure = setup_game_dictionary(input_data)

    # part one
    matches = find_sum_matches(game_data_structure)
    print('total for game one: ', sum_data(matches))

    #part two
    matches_two = find_maxs_games(game_data_structure)
    power_data = power_data(matches_two)
    print('total for game two: ', sum_data(power_data))

