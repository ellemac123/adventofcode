"""
https://adventofcode.com/2021/day/1

the answer for part one is:  1527
the answer for part two is:  1575
"""
def check_depth(sonar_values): 
    incrementals = 0
    for irb, echo in enumerate(sonar_values): 
        try: 
            if sonar_values[irb +1 ] > echo: 
                incrementals += 1
        except IndexError: 
            pass

    return incrementals

def main(): 
    sonar_values = []
    with open('input.txt', 'r') as f: 
        for a in f.readlines(): 
            sonar_values.append(int(a))
    
    print('the answer for part one is: ', check_depth(sonar_values))

    three_measurement_windows = [sum([sonar_values[a], sonar_values[a+1], sonar_values[a+2]]) for a in range(len(sonar_values)-2)]
    print('the answer for part two is: ', check_depth(three_measurement_windows))



if __name__ == "__main__": 
    main()