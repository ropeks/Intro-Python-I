"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

import sys
import calendar
from datetime import datetime

current_year = datetime.now().year
current_month = datetime.now().month

if len(sys.argv) == 3:
  year = sys.argv[2]
  month = sys.argv[1]
  try:
    print(calendar.TextCalendar().formatmonth(int(year), int(month)))
  except:
    sys.exit('invalid input!! please add month (1-12) and year (ex. 1984)')

elif len(sys.argv) == 2:
  month = sys.argv[1]
  try:
    print(calendar.TextCalendar().formatmonth(current_year, int(month)))
  except:
    sys.exit('invalid input!! please add month (1-12)')

elif len(sys.argv) == 1:
  try:
    print(calendar.TextCalendar().formatmonth(current_year, current_month))
  except:
    sys.exit("WTF?")

else:
  sys.exit('format: [filename] [month] (1-12) [year] (ex. 1984)')