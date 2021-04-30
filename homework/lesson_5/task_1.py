""""Task 1

The greatest number

Write a Python program to get the largest number from a list of random numbers with the length of 10

Constraints: use only while loop and random module to generate numbers"""

from random import randint

list_of_numbers = []
while len(list_of_numbers) < 11:
    list_of_numbers.append(randint(1, 10))
    print(f"The MAX number in list is {max(list_of_numbers)}")
