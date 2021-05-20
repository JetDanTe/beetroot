"""Task 2

Extend Phonebook application

Functionality of Phonebook application:

Add new entries
Search by first name
Search by last name
Search by full name
Search by telephone number
Search by city or state
Delete a record for a given telephone number
Update a record for a given telephone number
An option to exit the program


The first argument to the application should be the name of the phonebook. Application should load JSON data,
if it is present in the folder with application, else raise an error. After the user exits, all
data should be saved to loaded JSON.

"""

import json
import sys

try:
    phone_book = sys.argv[1]
except:
    raise Exception("Json phone book absent!")

answer = None


def new_person():
    new_person = {'First name': input("Enter fisrt name:\n"),
                  'Last name': input("Enter lastname:\n"),
                  'Full name': input("Enter firstname:\n"),
                  'Telephone number': input("Enter telephone number:\n"),
                  'City': input("Enter city:\n"),
                  'State': input("Enter state:\n")}
    with open("phone_book.json", "r") as phone_book_file:
        read_json = json.load(phone_book_file)
        read_json.append(new_person)
    with open("phone_book.json", "w") as phone_book_file:
        json.dump(read_json, phone_book_file)
    print("Succesful added!")


def show_card(person, greeting):
    card = (f"""Full name: {person['Full name']}
First name: {person['First name']}
Last name: {person['Last name']}
Telephone number: {person['Telephone number']}
City: {person['City']}
State: {person['State']}""")
    print(f"""You are {greeting}:\n{card}""")


def searching(object):
    with open(phone_book, "r") as phone_book_file:
        read_json = json.load(phone_book_file)
        for i in read_json:
            for j in i.values():
                if j.isdigit() == True:
                    if object in j:
                        return i
                    else:
                        pass
                elif j.isdigit() == False:
                    if object == j:
                        return i


def deleting(person_dict):
    with open(phone_book, "r") as phone_book_file:
        read_json = json.load(phone_book_file)
        for i in read_json:
            if i['Telephone number'] == person_dict['Telephone number']:
                show_card(person_dict, "deleting")
                read_json.remove(i)
    with open(phone_book, "w") as phone_book_file:
        json.dump(read_json, phone_book_file)


def updating(person_dict):
    with open(phone_book, "r") as phone_book_file:
        read_json = json.load(phone_book_file)
        for i in read_json:
            if i['Telephone number'] == person_dict['Telephone number']:
                answer = input(f"""Choose what field do you want to update:
1. First name, type 1.
2. Last name,type 2.
3. Full name, type 3.
4. Telephone number, type 4.
5. City, type 5.
6. State, type 6.\n""")
                if int(answer) == 1:
                    i['First name'] = input("Enter fisrt name:\n")
                elif int(answer) == 2:
                    i['Last name'] = input("Enter lastname:\n")
                elif int(answer) == 3:
                    i["Full name"] = input("Enter firstname:\n")
                elif int(answer) == 4:
                    i['Telephone number'] = input("Enter telephone number:\n")
                elif int(answer) == 5:
                    i['City'] = input("Enter city:\n")
                elif int(answer) == 6:
                    i['State'] = input("Enter state:\n")
    with open(phone_book, "w") as phone_book_file:
        json.dump(read_json, phone_book_file)



while answer != 9:
    answer = int(input("""Choose required menu point:
1. Add new contact, type 1.
2. Search by first name, type 2.
3. Search by last name, type 3.
4. Search by full name, type 4.
5. Search by telephone number, type 5.
6. Search by city or state, type 6.
7. Delete by tel. number, type 7.
8. Update by tel. number, type 8.
9. Quit, type 9.
"""))
    if answer == 1:
        new_person()
    elif answer == 2:
        show_card(searching(input("Enter first name:\n")), "looking for")
    elif answer == 3:
        show_card(searching(input("Enter last name:\n")), "looking for")
    elif answer == 4:
        show_card(searching(input("Enter full name:\n")), "looking for")
    elif answer == 5:
        show_card(searching(input("Enter telephone number:\n")), "looking for")
    elif answer == 6:
        show_card(searching(input("Enter city or state:\n")), "looking for")
    elif answer == 7:
        deleting(searching(input("Enter telephone number:\n")))
    elif answer == 8:
        updating(searching(input("Enter telephone number:\n")))
    elif answer == 9:
        break
