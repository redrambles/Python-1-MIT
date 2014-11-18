import string

def buildCoder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation, numbers and spaces.

    shift: 0 <= int < 26
    returns: dict
    """
    coder = {} # empty dict

    lower = string.ascii_lowercase # lower alphabet
    upper = string.ascii_uppercase # higher alphabet

    lowerShift = zip(lower, (lower[shift:] + lower[:shift])) # creates list of tuples, pairing one
    # letter with a shifted letter
    upperShift = zip(upper, (upper[shift:] + upper[:shift])) # same as above

    coder = dict(lowerShift + upperShift) #transforms list of tuples into dictionnary
    # which includes lowercase AND uppercase letters and their corresponding shifted
    # counterparts
    
    return coder
