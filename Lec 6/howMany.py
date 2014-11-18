def howMany(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    count = 0
    
    for valueList in aDict.values():
        count += len(valueList)
        
    return count
