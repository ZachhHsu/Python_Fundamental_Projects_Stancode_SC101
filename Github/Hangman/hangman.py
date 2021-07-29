"""
File: hangman.py
Name: Zach Hsu
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    # Display the dashed word and turns remained
    turns_remained = N_TURNS
    word = random_word()
    old_word = ''
    print('The word looks like: ', end='')
    for i in range(len(word)):
        old_word += '-'
    print(old_word)
    print('You have ' + str(turns_remained) + ' guesses left.')

    # Create a scaffold
    scaffold()
    for k in range(8):                                 # left and right poles
        print('|               |')

    # Start guessing the word
    while True:
        guess = input('Your guess: ')
        if guess.isalpha() and len(guess) == 1:        # case insensitive
            guess = guess.upper()
            new_word = ''                              # set up an empty string for the new guessing result this round

            # Correct guess
            if guess in word:
                for j in range(len(word)):

                    # Restore already correctly guessed characters
                    if old_word[j].isalpha():
                        new_word += old_word[j]

                    # Add correct and not yet guessed characters
                    elif guess == word[j]:
                        new_word += guess

                    # Dashed undiscovered slots
                    else:
                        new_word += '-'
                print('You are correct!')

                # Win the game if all dashes are un-dashed
                if '-' not in new_word:
                    print('You win!!')
                    print('The word was: ' + new_word)
                    break
                print('The word looks like: ' + new_word)

                # Update the new guessing result to old_word
                old_word = new_word

            # Incorrect guess
            else:
                turns_remained -= 1                    # lose one turn
                print('There is no ' + guess + '\'s in the word.')
                # Hang body parts
                hang(turns_remained)

                # Loose the game if no turns are left
                if turns_remained == 0:
                    print('You are completely hung : (')
                    print('The word was: ' + word)
                    break
            print('You have ' + str(turns_remained) + ' guesses left.')

        # Illegal format
        else:
            print('illegal format.')


def hang(n):
    """
    Hang body parts
    """
    # Head
    if n == 6:
        scaffold()
        print('|    ( * * )    |')
        print('|    (  V  )    |')
        for i in range(6):
            print('|               |')

    # Body
    elif n == 5:
        scaffold()
        print('|    ( * * )    |')
        print('|    (  V  )    |')
        print('|       #       |')
        print('|       #       |')
        print('|       #       |')
        print('|               |')
        print('|               |')
        print('|               |')

    # Left arm
    elif n == 4:
        scaffold()
        print('|    ( * * )    |')
        print('|    (  o  )    |')
        print('|       #       |')
        print('|   ~ ~ #       |')
        print('|       #       |')
        print('|               |')
        print('|               |')
        print('|               |')

    # Right arm
    elif n == 3:
        scaffold()
        print('|    ( * * )    |')
        print('|    (  o  )    |')
        print('|       #       |')
        print('|   ~ ~ # ~ ~   |')
        print('|       #       |')
        print('|               |')
        print('|               |')
        print('|               |')

    # Left leg
    elif n == 2:
        scaffold()
        print('|    ( Q Q )    |')
        print('|    (  W  )    |')
        print('|       #       |')
        print('|   ~ ~ # ~ ~   |')
        print('|       #       |')
        print('|      /        |')
        print('|      \\        |')
        print('|               |')

    # Right leg
    elif n == 1:
        scaffold()
        print('|    ( Q Q )    |')
        print('|    (  W  )    |')
        print('|       #       |')
        print('|   ~ ~ # ~ ~   |')
        print('|       #       |')
        print('|      / \\      |')
        print('|      \\ /      |')
        print('|               |')

    else:
        scaffold()
        print('|    ( X X )    |')
        print('|    (  ^  )    |')
        print('|       #       |')
        print('|   ~ ~ # ~ ~   |')
        print('|       #       |')
        print('|      / \\      |')
        print('|      \\ /      |')
        print('|               |')


def scaffold():
    """
    Create a scaffold
    """
    print('<Your Status>')
    print('-----------------')
    print('|       |       |')
    print('|       |       |')


def random_word():
    """
    Here are some random vocabularies to be guessed
    """
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
