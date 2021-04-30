"""Task 2

Exclusive common numbers.

Generate 2 lists with the length of 10 with random integers from 1 to 10, and make a third list
containing the common integers between the 2 initial lists without any duplicates.

Constraints: use only while loop and random module to generate numbers"""

from random import randint

list_of_numbers_1 = []
list_of_numbers_2 = []
list_of_numbers_3 = set()

while len(list_of_numbers_1) < 11:
    list_of_numbers_1.append(randint(1, 10))
    list_of_numbers_2.append(randint(1, 10))

for i in list_of_numbers_1:
    if i in list_of_numbers_2:
        list_of_numbers_3.add(i)

print(f"The 1st list contains: {list_of_numbers_1}.\nThe 2nd list contains: {list_of_numbers_2}.\n"
      f"The uniq list of numbers contains: {list_of_numbers_3}.")

