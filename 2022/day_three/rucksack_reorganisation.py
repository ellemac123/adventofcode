"""
https://adventofcode.com/2022/day/3

the solution for part one is:  7850
the solution for part two is:  2581
"""
def organise_lists(file_input_list):
    """
        Given an ugly input file
        remove the newlist
        add to a list where each row contains 2 lists:
            the first half and the second half of the string
    """
    final = []
    for line in file_input_list:
        split_line = list(line.strip())
        split = int(len(line)/2)
        final.append([split_line[:split], split_line[split:]])

    return final

def find_twins(split_list):
    """
        Given a split list, find all commonalities
        return the twins
    """
    twins = []
    for a in split_list:
        for b in a[0]:
            if b in a[1]:
                twins.append(b)
                break

    return twins

def find_twin_sum(twin_list):
    """
        Get the associated numerical value of each letter and return the total sum
        reference:
            Lowercase item types a through z have priorities 1 through 26.
            Uppercase item types A through Z have priorities 27 through 52.
    """
    total = 0
    for letter in twin_list:
        int_letter = ord(letter) - 96
        if int_letter < 0:
            # lowercase the letter bec its negative otherwise
            a = letter.lower()
            # subtract 70 because we want to subtract 96 since its ascii
            # then add 26 for the lowercase letters a-z
            int_letter = ord(a) + 26 - 96
        total = total + int_letter
    return total


def organise_part_two(file_input_list):
    """
    Given an ugly input file
    Split into a list of lists
    where each row contains 3 lists,
        one for each of the elves
    return the newly formatted list
    """
    finals = []
    # create an iterator of the input list
    file_input_list = iter(file_input_list)

    # zip through each of the file input lines
    for one, two, three in zip(file_input_list, file_input_list, file_input_list) :
        # create a list with 3 of the rows
        finals.append([list(one.strip()), list(two.strip()), list(three.strip())])
    return finals

def find_triplets(triplet_list):
    triplets = []
    for triplet in triplet_list:
        # find triplet thats the shortest
        # loop through and see if its in both
        first_triple = set(triplet[0])
        for item in first_triple:
            if item in triplet[1] and item in triplet[2]:
                triplets.append(item)
    return triplets

if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        a = f.readlines()

    # Part One Solution!!
    split_list = organise_lists(a)
    twins = find_twins(split_list)
    sum_ = find_twin_sum(twins)

    print('the solution for part one is: ', sum_)

    # Part Two Solution!
    part_two_organisation_list = organise_part_two(a)
    triplets = find_triplets(part_two_organisation_list)
    sum_two = find_twin_sum(triplets)

    print('the solution for part two is: ', sum_two)
