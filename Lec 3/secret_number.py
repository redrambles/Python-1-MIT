low = 0
high = 100
guess = 50
print ("Please think of a number between 0 and 100!")
print ("Is your secret number ") + str(guess) + ("?")
ans = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
while True:
    
    if ans == 'c':
        print ("Game over. Your secret number was: ") + str(guess)
        break
    
    elif ans == 'h':
        high = guess
        guess = (high + low) / 2
        print ("Is your secret number ") + str(guess) + ("?")
        ans = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    elif ans == 'l':
        low = guess
        guess = (high + low) / 2
        print ("Is your secret number ") + str(guess) + ("?")
        ans = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    else:
        print ("Sorry, I did not understand your input.")
        print ("Is your secret number ") + str(guess) + ("?")
        ans = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")

