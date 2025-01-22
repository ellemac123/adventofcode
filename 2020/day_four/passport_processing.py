"""
https://adventofcode.com/2020/day/4

The solution for part one is: 196
"""
from collections import defaultdict
import re

PASSPORT_INFORMATION = {
    "byr": re.compile(r'\d\d\d\d'), # birth year
    "iyr": re.compile(r'\d\d\d\d'), # Issue Year
    "eyr": re.compile(r'\d\d\d\d'), # expiration year
    "hgt": re.compile(r'\d\d'), # (Height)
    "hcl": re.compile(r'\d\d\d\d'), #(Hair Color)
    "ecl": re.compile(r'\d\d\d\d'), #(Eye Color)
    "pid": re.compile(r'\d\d\d\d'), #(Passport ID)
    # "cid", -- we can ignore this one
}


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

def check_passport_validity_full(passport_dict): 
    valid_passports = 0
    for pp in passport_dict: 
        if all(key in pp.keys() for key in PASSPORT_INFORMATION):
            flag = True
            for key in PASSPORT_INFORMATION.keys(): 
                if not re.match(PASSPORT_INFORMATION[key], pp[key]):
                    flag = False

            if flag:
                valid_passports +=1
    
    return valid_passports


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
    total_valid_passports_two = check_passport_validity_full(formatted_passports)

    return total_valid_passports, total_valid_passports_two


if __name__ == "__main__": 
    valid_passports, valid_passports_two = run()

    print('The solution for part one is:', valid_passports)
    print('The solution for part two is:', valid_passports_two)