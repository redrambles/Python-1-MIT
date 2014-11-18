def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
      * If the user inputs 'n', let the user play a new (random) hand.
      * If the user inputs 'r', let the user play the last hand again.
      * If the user inputs 'e', exit the game.
      * If the user inputs anything else, tell them their input was invalid.
 
    2) When done playing the hand, repeat from step 1    
    """
    n = HAND_SIZE # As specified by the exercise instructions
    count = 0

    while True:

        user = raw_input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")

        if user == 'e':
            break

        elif user == 'n':
            hand = dealHand(n) # deals new hand
            playHand(hand, wordList, n)
            print ("")
            count += 1
            
        elif user == 'r':

            if count == 0:
                print("You have not played a hand yet. Please play a new hand first!")
                print("")

            else:
                # did not call 'dealHand(n)' so the previous hand is replayed
                playHand(hand, wordList, n)
                print ("")
                
        else:
            print("Invalid command.")
            print ("")
