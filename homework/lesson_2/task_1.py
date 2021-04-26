"""Task 1

The greeting program.

Make a program that has your name and the current day of the week stored as separate variables and then prints a message like this:

     “Good day <name>! <day> is a perfect day to learn some python.”


Note that <name> and <day> are predefined variables in source code.

An additional bonus will be to use different string formatting methods for constructing result string."""

from datetime import date
from datetime import date

week = {1: 'Monady', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday', 7: 'Sunday'}
my_date = date.today()
key = my_date.weekday()
if key in week:
    print(f'''Good day {input("What is your name? ")}!
{week[key]} is a perfect day to learn some Python!''')