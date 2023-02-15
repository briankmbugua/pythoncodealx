#!/usr/bin/python3.9
"""Nearly all computers count time from an instant called the unix epoch, This occured in january 1, 1970 at 00:00:00 UTC
You can figure out the date and time in UTC of any given instant since january 1, 1970 by counting the number of seconds since the unix epoch, with the exception of leap seconds.Leap seconds all occasionally added to UTC to account for the slowing of the Earth's rotation but are not added to unix time"""

import time
# i = 0
# timebeforeWhile = time.time()
# print(timebeforeWhile)
# while i<100000:
#     print(time.time() - timebeforeWhile)
#     i = i+1

print(time.time())

#ISO 8601
# YYYY-MM-DD HH:MM:SS
#TIME MODULES IN PYTHON
#calendar -- outputs calenders and provides functions using an idealized Gregorian calender
#datetime -- supplies classes for manipulating date and times
#time -- provides time-related functions where dates are not needed

#time is less powerful and more complicated to use than datetime

#datetime
#datetime provides three classes
#1.datetime.date
#2.datetime.time
#3.datetime.datetime

from datetime import date, time, datetime
print(f"from date - {date(year=2000,month=1,day=31)}")
print(f"from time {time(hour=13,minute=14,second=31)}")
print(f"from datetime {datetime(year=2020, month=1,day=31,hour=13,minute=14,second=31)}")
print("today")
today = date.today() #creates a datetime.date instance with the current local date
print(f"today{today}")
print("now")
print(datetime.now()) #creates a datetime.datetime instance with the current local date and time
now = datetime.now()
current_time = time(now.hour, now.minute, now.second)
print(current_time)
print(datetime.combine(today, current_time)) #combines instances of datetime.date and datetime.time into a single datetime.datetime instance


