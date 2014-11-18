def biggestValue(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    result = 0
    answer = None
    
    for key in aDict.keys():
        if len(aDict[key]) >= result:
            result = len(aDict[key])
            answer = key
            
    return answer
        
        
        
