def myLog(x, b):
    '''
    x: a positive integer
    b: a positive integer; b >= 2

    returns: log_b(x), or, the logarithm of x relative to a base b.
    '''
    count = 0
    total = b
    
    while total <= x:
        total *= b
        count +=1

    return count
