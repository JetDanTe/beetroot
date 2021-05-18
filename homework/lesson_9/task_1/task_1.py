"""Task 1

Files

Write a script that creates a new output file called myfile.txt and writes the string "Hello file world!" in it.
Then write another script that opens myfile.txt, and reads and prints its contents. Run your two scripts from
the system command line.

Does the new file show up in the directory where you ran your scripts?

What if you add a different directory path to the filename passed to open?

Note: file write methods do not add newline characters to your strings; add an explicit ‘\n’ at the end of the
string if you want to fully terminate the line in the file.

"""
import os

file_name = 'test_file_1'

def file_create(greeting, file_name_):
    with open(file_name_, 'w') as g:
        g.write(greeting)

def read_file(file_name_):
    with open(file_name_, "r") as g:
        print(g.read())

file_create('Hello file world!\n', file_name)
read_file('test_file_1')

os.system(f'rm -rf {file_name}')