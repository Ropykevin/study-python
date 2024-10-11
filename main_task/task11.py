# # TASK 11: Using Python or PHP or Java or Ruby or JavaScript
# # Write a program that takes the date of birth of a person and the program outputs the age in terms of years, months, days TODAY.
# # Once you learn functions, revisit this and write this code inside a function.
import datetime

today = datetime.datetime.now()
print(today.day)#current day
print(today.month)  # current month
print(today.year)  # current year
dob=input("enter dob (yy/mm/dd):")#2000/4/24
# print(dob)

# dob=input("enter dob (yy/mm/dd):")
dob_split=dob.split("/")

dob_year = int(dob_split[0])
dob_month = int(dob_split[1])
dob_day = int(dob_split[2])

years=today.year-dob_year
months=today.month-dob_month
days=today.day-dob_day

if months<0:
    years-=1
    months=12+months

print(f"age:{years} years {months} months {days} days")

