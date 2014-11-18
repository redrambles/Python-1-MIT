def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    handCopy = hand.copy()
    remaining = []
    original = []
        
    for letter in handCopy.keys(): # gets the letters of the hand
        for j in range (handCopy[letter]): # in case there are more than one of same letter
            original.append(letter)
    
    for letter in word:
            if letter in handCopy.keys() and handCopy[letter] > 0:
                handCopy[letter] = handCopy.get(letter, 0) -1

    for letter in handCopy.keys(): # gets the letters of the hand
        for j in range (handCopy[letter]): # in case there are more than one of same letter
            remaining.append(letter)

    return word in wordList and len(remaining) + len(word) == len(original)
