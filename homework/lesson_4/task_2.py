"""Task 2

The birthday greeting program.

Write a program that takes your name as input, and then your age as input and greets you with the following:

“Hello <name>, on your next birthday you’ll be <age+1> years”   """

user_name, user_age = input("Enter your name, please!\n"), input("And enter your age, please!\n")
print(f"Hello, {user_name}!\nOn your next birthday you’ll be {int(user_age) + 1}, oldie =D")
