""""Make a program that has some sentence (a string) on input and returns
a dict containing all unique words
as keys and the number of occurrences as values. """
from pprint import pprint

some_input_string = input("Enter smth...\n")
some_chunks = some_input_string.split(' ')
some_dict = {}

for i in some_chunks:
    if i not in some_dict.items():
        some_dict[i] = 1
    elif i in some_dict.items():
        some_dict[i] += 1
        print(some_dict)

print(some_dict)
