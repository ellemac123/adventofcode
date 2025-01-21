"""
https://adventofcode.com/2020/day/4

The solution for part one is: 196
"""
from collections import defaultdict

PASSPORT_INFORMATION = (
    "byr", # birth year
    "iyr", # Issue Year
    "eyr", # expiration year
    "hgt", # (Height)
    "hcl", #(Hair Color)
    "ecl", #(Eye Color)
    "pid", #(Passport ID)
    # "cid", -- we can ignore this one
)


def check_passport_validity(passport_dict): 
    valid_passports = 0
    for pp in passport_dict: 
        if all(key in pp.keys() for key in PASSPORT_INFORMATION):
            valid_passports +=1
    
    return valid_passports

def format_file(raw_input): 
    passports = []
    for entry in raw_input: 
        passport = defaultdict()
        for row in entry:
            items = row.split(' ')
            for i in items: 
                xi = i.split(':')
                passport[xi[0]] = xi[1]
        passports.append(passport)

    return passports

def run(): 
    input = []
    with open('input.txt', 'r') as f: 
        value = []
        for a in f.readlines(): 
            if a == "\n": 
                input.append(value)
                value = []
            else: 
                value.append(a.strip())
        input.append(value)
   
    formatted_passports = format_file(input)

    total_valid_passports = check_passport_validity(formatted_passports)

    return total_valid_passports


if __name__ == "__main__": 
    valid_passports = run()

    print('The solution for part one is:', valid_passports)