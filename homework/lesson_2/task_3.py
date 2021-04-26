"""Task 3

Using python as a calculator.

Make a program with 2 numbers saved in separate variables a and b, then print the result for each of the following:

Addition
Subtraction
Division
Multiplication
Exponent (Power)
Modulus
Floor division"""

first_int = int(input("Enter first number\n"))
second_int = int(input("Enter second number\n"))

print(f'Addition of numbers: {first_int + second_int}\nSubtraction of numbers: {first_int - second_int}\n'
      f'Division of numbers: {first_int / second_int}\nMultiplication of numbers: {first_int - second_int}\n'
      f'Exponent (Power) of numbers: {first_int ** second_int}\nModulus of numbers: {first_int % second_int}\n'
      f'Floor division of numbers: {first_int // second_int}')
