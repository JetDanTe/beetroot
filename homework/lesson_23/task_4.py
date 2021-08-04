"""Task 4

def reverse(input_str: str) -> str:
    Function returns reversed input string
    reverse("hello") == "olleh"
    reverse("o") == "o"
    """

def reverse(input_str: str) -> str:
    if len(input_str) == 0:
        return input_str
    else:
        return reverse(input_str[1:]) + input_str[0]

if __name__ == '__main__':
    print(reverse("hello"))