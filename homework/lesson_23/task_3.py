"""#############################################
# All tasks should be solved using recursion
#############################################
Task 3

from typing import Optional
def mult(a: int, n: int) -> int:

    This function works only with positive integers

    mult(2, 4) == 8
    True

    mult(2, 0) == 0
    True

    mult(2, -4)
    ValueError("This function works only with postive integers")
"""

def mult(a: int, n: int) -> int:
    if a == 0:
        return 0
    elif a == 1:
        return n
    elif n == 1:
        return a
    elif n < 0:
        raise ValueError(Exception, "This function works only with postive integers")
    else:
        return n + mult(a - 1, n)

if __name__ == '__main__':
    print(mult(2, 4))
    print(mult(2, 0))
    print(mult(2, -4))

