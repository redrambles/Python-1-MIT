def mcNuggets(n):
    """
    n is an int

    Returns True if some integer combination of 6, 9 and 20 equals n
    Otherwise returns False.
    """
    result = []

    if n % 20 == 0 or n % 9 == 0 or n % 6 == 0:
            return True            
    
    else:
        result = n % 20

        if result % 9 == 0 or result % 6 == 0:
            return True

        else:
            result = result % 9

            if result % 6 == 0:
                return True

            else:
                return False



