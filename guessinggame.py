"""1) The computer must generate a different random number from 1 to 100 each time the game is played.
2) The game should repeat until the user guesses the correct number.
3) If the user picks a number that is too high, the program should tell the user that their choice was too high.
4) If the user picks a number that is too low, the program should tell the user that their choice was too low."""


# pseudocode
# Random 1 to 100
# Loop
# Input
# Print if too high or too low
# If win, quit the loop

import random

question = random.randint(1, 100)
while True:
    answer = input("Please enter a number from 1 to 100: ")
    if int(answer) > question:
        print("Your number is too high.")
    elif int(answer) < question:
        print("Your number is too low.")
    elif int(answer) == question:
        print("You guessed the correct number!")
        break
