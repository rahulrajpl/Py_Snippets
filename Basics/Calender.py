"""
This program will print the calendar for the current month of the current year
Author: coder233
"""

import calendar
from datetime import datetime


print("This Month's calendar for you...!")
print(calendar.month(datetime.now().year,datetime.now().month))