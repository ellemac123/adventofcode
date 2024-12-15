inputRow =  ['44', '45', '46', '47', '48', '48']
removal = 0 

def isDecrementing(inputRow): 
    removal = 0
    for i in range(len(inputRow)-1): 
        diff = int(inputRow[i+1]) - int(inputRow[i])
        if (diff > 3 or diff < 1):
            if removal == 0: 
                if i == 0 and (len(inputRow) > i+2): 
                    diff = int(inputRow[i+2]) - int(inputRow[i])

                    if (diff <= 3 or diff >= 1): 
                        i = i + 1 
                        removal = removal +1  
                    else:      
                        return False
                else: 
                    if (len(inputRow) > i+1 and i-1 >= 0 ):
                        diff = int(inputRow[i+1]) - int(inputRow[i-1])
                        if (diff > 3 or diff < 1): 
                            return False
                        else: 
                            removal = removal + 1
                    else: 
                        return False
            else: 
                return False
    return True

decRow = ['48', '46', '44', '43', '43', '42']

def isIncrementing(inputRow):  
    removal = 0
    for i in range(len(inputRow)-1): 
        diff = int(inputRow[i+1]) - int(inputRow[i])
        if (diff < -3 or diff >= 0): 
            if removal == 0: 
                if i == 0 and (len(inputRow) > i+2): 
                    diff = int(inputRow[i+2]) - int(inputRow[i])
                    if (diff < -3 or diff >= 0): 
                       print('returning flase here')
                       return False
                    else: 
                        i = i+1 
                        removal = removal + 1 
                else: 
                    print(len(inputRow))
                    print(i)
                    if (len(inputRow) >= i+1 and i > 0):
                        diff = int(inputRow[i+1]) - int(inputRow[i-1])
                        if (diff < -3 or diff >= 0): 
                            print('returning flase here 2')

                            return False 
                        else:      
                            removal = removal +1 
                    else: 
                        print('returning flase here 3')

                        return False
            else: 
                print('returning flase here 4')
                return False
    return True


# if decrementing 
# if i am in the first row and the next one is not duplicating, look two forward, if it is ok then increment the removal by 1 and increment i by one
# if i am not the first row, look back one and forward one - if that works then increment removal by 1


print(isIncrementing(decRow))
