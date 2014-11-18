secretWord = 'apple'

lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''

    word = []

    for c in secretWord:
        if c in lettersGuessed:
            word.append(c)
            
        else:
            word.append('_')


    return ' '.join(word)
