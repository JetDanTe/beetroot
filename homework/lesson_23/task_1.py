"""#############################################
# All tasks should be solved using recursion
#############################################
Task 1

from typing import Optional
def to_power(x: Optional[int, float], exp: int) -> Optional[int, float]:
    Returns  x ^ exp

    to_power(2, 3) == 8
    True

    to_power(3.5, 2) == 12.25
    True

    to_power(2, -1)
    ValueError: This function works only with exp > 0.
    pass"""

from typing import Optional

def to_power(x, exp):

    if exp == 1:
        return x * exp
    else:
        if exp <= 0:
            raise Exception(ValueError, "This function works only with exp > 0")
        else:
            return x * to_power(x, exp-1)



if __name__ == '__main__':
    print(to_power(2, 3) == 8)
    print(to_power(3.5, 2) == 12.25)
    print(to_power(2, -1))

