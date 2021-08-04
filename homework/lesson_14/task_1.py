"""Task 1

Write a decorator that prints a function with arguments passed to it.

NOTE! It should print the function, not the result of its execution!

For example:

 "add called with 4, 5"

```

def logger(func):

    pass



@logger

def add(x, y):

    return x + y



@logger

def square_all(*args):

    return [arg ** 2 for arg in args]

```"""

def logger(func):
    def deco_print(*args, **kwargs):
        return (f"Work with {func.__name__} function and with arguments {*args, *kwargs}")
    return deco_print



@logger
def add(x, y):
    return x + y



@logger
def square_all(*args):
    return [arg ** 2 for arg in args]

print(add(4,5))
print(square_all(4,5))

