"""Task 2

The valid phone number program.

Make a program that checks if a string is in the right format for a phone number. The program should check that the string contains only numerical characters and is only 10 characters long. Print a suitable message depending on the outcome of the string evaluation."""

phone_number = input("Enter phone number:\n")

if phone_number.isdigit():
    if len(str(phone_number)) == 10:
        print(f"Your phone number: {phone_number}.")
    elif len(str(phone_number)) < 10:
        forgotten_digits = 10 - int(len(str(phone_number)))
        print("You have been forgotten {} digits".format(forgotten_digits))
else:
    print("Phone numbers must contain digits only.")
