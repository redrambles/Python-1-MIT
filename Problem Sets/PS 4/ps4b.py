from ps4a import *
import time


#
#
# Problem #6: Computer chooses a word
#
#
def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: string or None
    """
    # Create a new variable to store the maximum score seen so far (initially 0)
    total = 0

    # Create a new variable to store the best word seen so far (initially None)
    bestWord = None

    # For each word in the wordList
    for word in wordList:

        # If you can construct the word from your hand
        # (hint: you can use isValidWord, or - since you don't really need to test if the word is in the wordList - you can make a similar function that omits that test)
        if isValidWord(word, hand, wordList):
            # Find out how much making that word is worth
            score = getWordScore(word, n)
            
            # If the score for that word is higher than your best score
            if score > total:

                # Update your best score, and best word accordingly
                total = score
                bestWord = word

    # return the best word you found.
    return bestWord


#
# Problem #7: Computer plays a hand
#
def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    # Keep track of the total score
    totalScore = 0
    remainingHand = 0
    word = compChooseWord(hand, wordList, n)

    
    # As long as there are still letters left in the hand:
    while n > 0:

        # Display the hand
        print("Current Hand: "),
        displayHand(hand)

        if compChooseWord(hand, wordList, n) == None:
            break
        
        else:

            # Computer chooses word
            word = compChooseWord(hand, wordList, n)
            
            if remainingHand == len(str(word)):
                tooMuch = (getWordScore(word, n)) - 50
                print ('"') + word +('"') + (" earned ") +  str(tooMuch) + (" points. Total: ") + str(totalScore + tooMuch) + (" points.")
                print("")
                break
        # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line
            else:
            
                totalScore += getWordScore(word, n)
                print ('"') + word +('"') + (" earned ") +  str(getWordScore(word, n)) + (" points. Total: ") + str(totalScore) + (" points.")
                print("")
        
        # Update the hand 
        hand = updateHand(hand, word)
        remainingHand = calculateHandlen(hand)
        n = remainingHand
        word = compChooseWord(hand, wordList, n)



    if remainingHand == len(str(word)):
        print("Total score: ") + str(totalScore + tooMuch) + (" points.")

    else:
        print("Total score: ") + str(totalScore) + (" points.")
    
#
# Problem #8: Playing a game
#
#
def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
      
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    n = HAND_SIZE # As specified by the exercise instructions
    count = 0

    while True:

        user = raw_input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
        print ("")

        if user == 'e':
            break

        

        if user == 'n':

            user2 = raw_input("Enter u to have yourself play, c to have the computer play: ")
            
            if user2 == 'u':
                print("")
                hand = dealHand(n) # deals new hand
                playHand(hand, wordList, n)
                print ("")
                count += 1

            elif user2 == 'c':
                print("")
                hand = dealHand(n) # deals new hand
                compPlayHand(hand, wordList, n)
                print ("")
                count += 1

            else:
                print("Invalid Command.")
                print("")
                
            
        elif user == 'r':

            
            if count == 0:
                print("You have not played a hand yet. Please play a new hand first!")
                print("")

            elif:

                user2 = raw_input("Enter u to have yourself play, c to have the computer play: ")
                
                if user2 == 'u':
                    print("")
                    playHand(hand, wordList, n)
                    print ("")

                elif user2 == 'c':
                    print("")
                    compPlayHand(hand, wordList, n)
                    print ("")

                else:
                    print("Invalid Command.")
                    print("")
                
        else:
            print("Invalid command.")
            print ("")


        
#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)


