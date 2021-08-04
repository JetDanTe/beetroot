"""Task 1

Write a Python program to detect the number of local variables declared in a function.

"""
def local_var_counter():
    ein = 1
    zwei = 2
    drei = 3
    fier = 4
    funf = 5

print(local_var_counter.__code__.co_nlocals)
