"""
The first section specifies the page ordering rules, one per line. The first rule, 47|53, means that if an update includes both page number 47 
and page number 53, then page number 47 must be printed at some point before page number 53. (47 doesn't necessarily need to be immediately before 53; other pages are allowed to be between them.)

The second section specifies the page numbers of each update. Because most safety manuals are different, 
the pages needed in the updates are different too. The first update, 75,47,61,53,29, means that the update consists of page numbers 75, 47, 61, 53, and 29.

To get the printers going as soon as possible, start by identifying which updates are already in the right order.

For some reason, the Elves also need to know the middle page number of each update being printed. 
Because you are currently only printing the correctly-ordered updates, you will need to find the middle 
page number of each correctly-ordered update. In the above example, the correctly-ordered updates are:

75,47,61,53,29
97,61,53,29,13
75,29,13
These have middle page numbers of 61, 53, and 29 respectively. Adding these page numbers together gives 143.

Of course, you'll need to be careful: the actual list of page ordering rules is bigger and more complicated than the above example.

Determine which updates are already in the correct order. What do you get if you add up the middle page number from those correctly-ordered updates?
"""
def page_ordering_rules_map(page_ordering_rules): 
    orderingDict = {}

    for i in page_ordering_rules:
        key = int(i[0])
        value = int(i[1])
        if key in orderingDict.keys(): 
            orderingDict[key].append(value)
        else: 
            orderingDict[key] = [value]

    return orderingDict

def sum_middles(input_list): 
    """
        given a list of values, get the middle value
    """
    middles = 0
    for i in input_list: 
        middles = middles + int(i[int((len(i) / 2))])
    return middles


def check_rule_row(row, page_rules): 
    """
    Given the row: for each value in the row, check its rules are correct
    """
    for val in row: 
        #check each index is right
        if val in page_rules:
            for rule in page_rules[val]: 
                if rule in row: 
                    if not row.index(val) < row.index(rule): 
                        return False
    return True


def check_list(page_rules, page_numbers_updates): 
    """
        Given a list of ordering rules and a list of page numbers

        for each list of page numbers, check that the ordering rules apply for each value

        if yes:
            get the middle value and append it to the list of middle values
    """
    list_of_middles = []

    for row in page_numbers_updates: 
        if check_rule_row(row, page_rules): 
            list_of_middles.append(row)

    return(sum_middles(list_of_middles))


if __name__ == "__main__": 
    with open('input.txt', 'r') as input_file:            
        inputString = input_file.read()
    
    page_ordering_rules = []
    page_numbers_updates = []

    for i in inputString.split('\n'):
        if i: 
            if '|' in i: 
                page_ordering_rules.append(i.split('|'))
            else: 
                page_numbers_updates.append([int(val) for val in i.split(',')])
    
    page_rules = page_ordering_rules_map(page_ordering_rules)

    print(check_list(page_rules, page_numbers_updates))