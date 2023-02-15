#!/usr/bin/python3.9
from datetime import date, datetime
date = date.fromisoformat("2020-01-31")
print(date)

#for none iso format dates that are in string format use strptime(), you have to tell python what each part of the string represents using formatting codes

date_string = "01-31-2020 14:45:37"
format_string = "%m-%d-%Y %H:%M:%S"
fromStringDate = datetime.strptime(date_string, format_string)
print(fromStringDate)

