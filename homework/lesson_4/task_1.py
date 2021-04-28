"""Task 1

The Guessing Game.

Write a program that generates a random number between 1 and 10 and lets the user guess what number was generated.
The result should be sent back to the user via a print statement."""

import random

guessed_number = random.randint(1, 11)
entered_number = int(input('Enter number, please. \n'))
try_again = True
while True:
    if entered_number == guessed_number:
        print(f'You guessed. Number is {guessed_number}.')
        break
    elif guessed_number != entered_number:
        print(f"You did not guess right. Great Random says {guessed_number}")
        break
    else:
        print("You do not enter anything!")
