'''
Student: Denver Ha
Description: Number Guessing Game
AM
'''

from random import * # Importing random

number = randint(1, 10) # Creating random integer
guesses = [] # Creating empty list for guesses
tries = 5 # Number of tries (extra credit)

# Main block of code
while True:
    guess = int(input("Enter an integer from 1-10: ")) # Getting an input from user
    if guess < 1 or guess > 10: # Determining if guess is in range
        print("Invalid guess, must be between 1 and 10")

    elif guess in guesses: # Determining if guess has already been used
        print("You already guessed this. Try again.")

    else: # Valid guess
        guesses.append(guess) # Adding guess to list
        tries -= 1
        if guess > number: # If guess is higher than the random integer
            print("Too high!")
            print("Previous guesses:", guesses)
            if tries == 0: # Ending the game if they use up 5 guesses
                print("You lose!!!")
                print("The number was:", number)
                break
            else:
                print("You have", tries, "tries remaining")

        elif guess < number: # If guess is lower than the random integer
            print("Too low!")
            print("Previous guesses:", guesses)
            if tries == 0: # Ending the game if they use up 5 guesses
                print("You lose!!!")
                print("The number was:", number)
                break
            else:
                print("You have", tries, "tries remaining")

        else: # Correct guess
            tries += 1
            print("Correct!")
            print("Your guesses:", guesses)
            print("Number of tries left:", tries)
            break


'''
Enter an integer from 1-10: 1
Too low!
Previous guesses: [1]
You have 4 tries remaining
Enter an integer from 1-10: 1
You already guessed this. Try again.
Enter an integer from 1-10: 2
Too low!
Previous guesses: [1, 2]
You have 3 tries remaining
Enter an integer from 1-10: 3
Too low!
Previous guesses: [1, 2, 3]
You have 2 tries remaining
Enter an integer from 1-10: 4
Too low!
Previous guesses: [1, 2, 3, 4]
You have 1 tries remaining
Enter an integer from 1-10: 5
Too low!
Previous guesses: [1, 2, 3, 4, 5]
You lose!!!
The number was: 6
'''