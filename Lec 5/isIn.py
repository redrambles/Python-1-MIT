def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''

    if aStr == '':
        return False

    if len(aStr) == 1:
        return aStr == char

    middle = len(aStr)/2
    midIndex = aStr[middle]

    
    if char == midIndex:
        return True
        
    elif char < midIndex:
        return isIn(char, aStr[:middle])

    else:
        return isIn(char, aStr[midle:])
