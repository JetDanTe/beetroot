"""Task 4

The math quiz program

Write a program that asks the answer for a mathematical expression, checks whether the user is right or wrong,
and then responds with a message accordingly."""

import random
import operator

first_int, second_int = random.randint(1,9), random.randint(1,9)
actions = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
random_action = random.choice(list(actions.keys())) #Зачем здесь метод list?
answer = actions.get(random_action)(first_int, second_int)
if len(str(answer)) > 3:
    print(f"Very long answer - {answer}.\nSorry, restart quiz, please.")
elif len(str(answer)) <= 2:
    while answer != int(input(f'Count {first_int}{random_action}{second_int}?\n')):
        print("Try again!")
    print("Correct!")

