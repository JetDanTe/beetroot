'''Task 2

Create a python program named “task2”, and use the built-in function `print` in it several times. Try to pass “sep”, “end” params and pass several parameters separated by commas.

Also, provide a comment text above each print statement, mentioned above, with the expected output after execution of the particular print statement.

(Ex.
# ‘hello world’
print(“hello world”)
)'''

# User input
user_input = input('Enter something, please...\n')
user_input_list = user_input.split(" ")
separators = ("-", "*", "!", "qq", "18+")
# User input check
print("You entered: '{}'".format(user_input))
# User input with capitalize method
print("Your capitalized text: '{}'".format(user_input.capitalize()), end = '\n---------\n')
# User input with upper-case method
print("Your upper-cased text: '{}'".format(user_input.upper()), end = '\n*********\n')
# User input with title method
print("Your titled text: '{}'".format(user_input.title()), end = '\n__________\n')


for s in separators:
    print(f"String will be separete by '{s}' :", "Smth", "went", "wrong...", sep=s, end = f'\n{len(user_input)*"_"}\n')


