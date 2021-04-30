"""Task 3

Extracting numbers.

Make a list that contains all integers from 1 to 100, then find all integers from the list that are divisible
by 7 but not a multiple of 5, and store them in a separate list. Finally, print the list.

Constraint: use only while loop for iteration"""

one_hundred_smt = []
counter = 1
seven_and_not_five = []

while len(one_hundred_smt) != 100:
    one_hundred_smt.append(counter)
    counter += 1
    if counter % 7 == 0 and counter % 5 != 0:
        seven_and_not_five.append(counter)

print(f"The numbers that are divisible by 7 and not a multiple of 5: {seven_and_not_five}." )