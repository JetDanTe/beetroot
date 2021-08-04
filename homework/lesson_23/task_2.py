"""#############################################
# All tasks should be solved using recursion
#############################################

Task 2

from typing import Optional
def is_palindrome(looking_str: str, index: int = 0) -> bool:

    Checks if input string is Palindrome
   is_palindrome('mom')
    True

   is_palindrome('sassas')
    True

    is_palindrome('o')
    True

    pass
"""

def is_palindrome(looking_str: str, index: int = 0) -> bool:
    if len(looking_str) <= 1:
        return True
    else:
        if looking_str[0] == looking_str[-1]:
            return is_palindrome(looking_str[1:-1])
        else:
            return False

if __name__ == '__main__':
    print(is_palindrome("mom"))
    print(is_palindrome("dante"))
    print(is_palindrome("o"))
    print(is_palindrome("sasdsas"))




