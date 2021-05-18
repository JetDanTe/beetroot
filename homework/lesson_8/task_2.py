"""Task 2

Write a function that takes in two numbers from the user via input(), call the numbers a and b, and then returns
the value of squared a divided by b, construct a try-except block which raises an exception if the two values given
by the input function were not numbers, and if value b was zero (cannot divide by zero).
"""

def calc(a, b):
    try:
        result = int(a) ** 2 / int(b)
        return result
    except ZeroDivisionError:
        return('Can not be divided by Zero!')
    except ValueError:
        return("It must be digits only!")



print(calc(input("Enter first number!\n"), input('Enter second number!\n')))
