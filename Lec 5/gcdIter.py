def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''

    smaller = min(a, b)
    larger = max (a, b)

    if min(a, b) == 0:
        return 0

    else:
        while smaller >= 1:

            if larger % smaller == 0 and min(a,b) % smaller == 0:
                return smaller

            else:
                smaller -= 1        
                
        
