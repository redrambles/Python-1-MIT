def hash(s):
    total = 0
    for char in s:
        total += string.ascii_lowercase.index(char)
    return total % 26

'''
This function relies on modular arithmetic, which many real-life hash functions
actually do use. The premise here is that we're summing the values of every
letter in the word, then modding that number by 26 to place it in one of the
26 buckets. This method is better than relying on a property (length, first/last
letter) that is likely to be shared by a large batch of words.
'''
