"""Task 1

Write a function called oops that explicitly raises an IndexError exception when called. Then write another function
that calls oops inside a try/except statement to catch the error. What happens if you change oops to
raise KeyError instead of IndexError?
"""

def oops(answer):
    if answer.lower == "index":
        raise IndexError
    elif answer.lower == "key":
        raise KeyError
    else:
        print('I wish U A Merry Christams!')
try:
    oops("lol")
except:
    print('Something another...')


