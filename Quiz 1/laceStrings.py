def laceStrings(s1, s2):
    """
    s1 and s2 are strings.

    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length, 
    then the extra elements should appear at the end.
    """
    laced = []

    if s1 == "":
        return s2

    if s2 == "":
        return s1

    
    while len(s1) > 0 and len(s2) > 0:

        laced.append(s1[0] + s2[0])

        s1 = s1[1:]
        s2 = s2[1:]

        if len(s1) == 0:
            laced.append(s2)

        elif len(s2) == 0:
            laced.append(s1)
            

    return "".join(laced)


        

    
