"""Task 2

Write a Python program to access a function inside a function (Tips: use function, which returns another function)

"""

def first_func(text):
    def second_func(text):
        new_text = ""
        counter = 0
        for i in text:
            if not counter & 1:
                new_text = f"{new_text}{i.lower()}"
            else:
                new_text = f"{new_text}{i.upper()}"
            counter += 1
        return new_text
    return second_func(text)




a = first_func("Olololo, ya vodeitel NLO")
print(a)
