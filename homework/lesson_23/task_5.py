"""Task 5

def sum_of_digits(digit_string: str) -> int:

 um_of_digits('26') == 8
    True

sum_of_digits('test')
    ValueError("input string must be digit string")
    """
def sum_of_digits(digit_string: str) -> int:
        if digit_string == "":
            return 0
        else:
            return int(digit_string[0]) + sum_of_digits(digit_string[1:])

if __name__ == '__main__':
    print(sum_of_digits("26"))
    print(sum_of_digits("test"))