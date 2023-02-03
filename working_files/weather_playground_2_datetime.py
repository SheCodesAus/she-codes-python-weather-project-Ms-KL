import csv
from datetime import datetime

# my code:
# cd C:\GIT\python-assignment\she-codes-python-weather-project-Ms-KL
# python weather_playground_2_datetime.py

# DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"


# def convert_date(iso_string):
#     """Converts and ISO formatted date into a human readable format.

#     Args:
#         iso_string: An ISO date string..
#     Returns:
#         A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
#     """

#     pass


# ------------------ EXAMPLE
# https://www.folkstalk.com/2022/10/python-datetime-from-isoformat-with-code-examples.html

# https://www.programiz.com/python-programming/datetime/strftime

iso_string = "2021-07-05T07:00:00+08:00"
date_time = datetime.fromisoformat(iso_string)
convert_date = date_time.strftime("%A %d %B %Y")
print(iso_string)
print(date_time)
print(convert_date)

# print(iso_string.isoformat())
# t = datetime.strptime(iso_string, "%Y-%m-%dT%H:%M:%S%z")
# time = t.strptime(iso_string, "%d %B %Y")
# print(t)


# convert string in iso 8601 date dime format to python datetime type
# converted = datetime.strptime(iso_string, "%Y-%m-%dT%H:%M:%SZ")
# print(converted)

# print(convert_date(2022-11-20))


# print(iso_string)

# print("------------------------")


# # Get current ISO 8601 datetime in string format
# iso_date = iso_string.isoformat()
# print(iso_date)



# from datetime import datetime

# dt = datetime()

# # convert datetime to ISO date
# iso_date = dt.isoformat()
# print('ISO Date:', iso_date)



# year = int(input('Enter a year'))
# month = int(input('Enter a month'))
# day = int(input('Enter a day'))
# date1 = datetime.date(year, month, day)


# time=datetime.strptime(iso_string, "%Y-%m-%d") 
# print(time)

# year, month, day = map(int, iso_string.split('-'))
# date1 = datetime.date(year, month, day)

# print(date1)

 
# Create datetime string
# iso_string = "2021-07-05T07:00:00+08:00"
# print("datetime string : {}".format(iso_string))
 
# # call datetime.strptime to convert
# # it into datetime datatype
# datetime_obj = datetime.strptime(iso_string,"%d%m%y%H%M%S")
 
# # It will print the datetime object
# print(datetime_obj)
 
# # extract the time from datetime_obj
# date = datetime_obj.date()
 
# # it will print date that we have
# # extracted from datetime obj
# print(date)