"""
Part one:
Appreciative of your help yesterday, one Elf gives you an encrypted
strategy guide (your puzzle input) that they say will be sure to help you win.
"The first column is what your opponent is going to play: A for Rock, B for Paper, and C for Scissors.
The second column--" Suddenly, the Elf is called away to help with someone's tent.

The second column, you reason, must be what you should play in response: X for Rock,
Y for Paper, and Z for Scissors. Winning every time would be suspicious, so the responses must have
been carefully chosen.

The winner of the whole tournament is the player with the highest score. Your total score is
the sum of your scores for each round. The score for a single round is the score for the shape
you selected (1 for Rock, 2 for Paper, and 3 for Scissors) plus the score for the outcome of the round (0 if you lost,
3 if the round was a draw, and 6 if you won).

Since you can't be sure if the Elf is trying to help you or trick you, you should
calculate the score you would get if you were to follow the strategy guide.

For example, suppose you were given the following strategy guide:

A Y
B X
C Z
This strategy guide predicts and recommends the following:

In the first round, your opponent will choose Rock (A), and you should choose Paper (Y). This ends in a win for you
with a score of 8 (2 because you chose Paper + 6 because you won).
In the second round, your opponent will choose Paper (B), and you should choose Rock (X).
This ends in a loss for you with a score of 1 (1 + 0).
The third round is a draw with both players choosing Scissors, giving you a score of 3 + 3 = 6.
In this example, if you were to follow the strategy guide, you would get a total score of 15 (8 + 1 + 6).

What would your total score be if everything goes exactly according to your strategy guide?
Solution for part one:  12156
Solution for part two:  10835

"""
SCORES = {
    'X': 1,
    'Y': 2,
    'Z': 3,
    'draw': 3,
    'win': 6,
    'loss': 0,
}

# x - lose, y - draw, z - win
SCORES_TWO = {
    'Y': 3,
    'Z': 6,
    'X': 0,
}
# Rock: A or X
# Paper: B or Y
# Scissors: C or Z
GAMES = {
    'X':{
        'A': 'draw',
        'B': 'loss',
        'C': 'win',
    },
    'Y':{
        'A': 'win',
        'B': 'draw',
        'C': 'loss',
    },
    'Z':{
        'A': 'loss',
        'B': 'win',
        'C': 'draw',
    },
    'A': {
        # ROCK: A
        'X': 3, # lose - scissors
        'Y': 1, # draw - rock
        'Z': 2, # i win - paper
    },
    'B': {
        # Paper: B
        'X': 1, # i lose - rock (1)
        'Y': 2, # i draw - paper (2)
        'Z': 3, # i win - scissors (3)
    },
    'C': {
        # Scissors: C
        'X': 2, # i lose - paper (2)
        'Y': 3, # i draw - scissors (3)
        'Z': 1, # i win - rock (1)
    }
}

PART_TWO_MATCH = {
    'X': 'loss',
    'Y': 'draw',
    'Z': 'win',
}

def score_round_part_one(your_turn, my_turn):
    """
    Given input, return a score
    """
    result = GAMES[my_turn][your_turn]
    score = SCORES[my_turn] + SCORES[result]

    return score

def score_round_part_two(your_turn, outcome):
    """
    Given their input, and required outcome, return a score
    """
    score = GAMES[your_turn][outcome] + SCORES_TWO[outcome]
    return score


def game_play(game):
    game_score = 0
    part_two_game_score = 0
    for match in game:
        opponents = match.strip().split(' ')
        score = score_round_part_one(opponents[0], opponents[1])
        part_two_score = score_round_part_two(opponents[0], opponents[1])

        part_two_game_score = part_two_game_score + part_two_score
        game_score = game_score + score

    return game_score, part_two_game_score

if __name__ == "__main__":
    with open('input.txt') as f:
        input_file = f.read()

    rounds = input_file.split('\n')

    total_score, part_two_score = game_play(rounds)

    print('Solution for part one: ', total_score)
    print('Solution for part two: ', part_two_score)
