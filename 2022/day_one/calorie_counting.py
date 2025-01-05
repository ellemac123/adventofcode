"""
Part 1:
The jungle must be too overgrown and difficult to navigate in vehicles or access
from the air; the Elves' expedition traditionally goes on foot. As your boats
approach land, the Elves begin taking inventory of their supplies. One important
consideration is food - in particular, the number of Calories each Elf is
carrying (your puzzle input).

The Elves take turns writing down the number of Calories contained by the
various meals, snacks, rations, etc. that they've brought with them, one
item per line. Each Elf separates their own inventory from the previous Elf's
inventory (if any) by a blank line.

Find the Elf carrying the most Calories. How many total Calories
is that Elf carrying?

Part 2:
Get the top 3 elves and sum them.

Solution for part one:  75622
Solution for part two:  213159
"""
def find_max_calories(caloric_input):
    """
    Given file input
    split it by double new lines
    then loop over and if the value is higher than the max value
    set max value

    return max_value calories in the list
    """
    elves_list = caloric_input.split('\n\n')
    calories = []
    for elf in elves_list:
        max_calories = sum([int(val) for val in elf.strip().split('\n')])
        calories.append(max_calories)

    calories.sort(reverse=True)
    return calories


if __name__ == "__main__":
    with open('input.txt') as f:
       file_input = f.read()

    calories_list = find_max_calories(file_input)

    print('Solution for part one: ', calories_list[0])
    print('Solution for part two: ', sum(calories_list[:3]))