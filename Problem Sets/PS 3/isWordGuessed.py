secretWord = 'apple'
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']

def isWordGuessed(secretWord, lettersGuessed):

    guess = []

    for c in secretWord:
        if c in lettersGuessed:
            guess.append(c)

    return len(guess) == len(secretWord)
    
