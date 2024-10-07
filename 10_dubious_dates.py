
from datetime import datetime #import the datetime class from the datetime module

"""
Exercise 1:
Write a Python program that prints the current date and time using the datetime module.
"""


current_datetime = datetime.now() # using the now thing to get their date and time at the current moment
print("Current date and time:", current_datetime)


"""
Exercise 2:
Write a Python program that prints the current date and time using the datetime module.
Using the strftime function format the date in standard U.S. date format (MM/DD/YYYY)
"""

current_datetime = datetime.now()  #get the current date and time
formatted_date = current_datetime.strftime("%m/%d/%Y")  #formatting the date using strftime in MM/DD/YYYY format
print("Formatted date (MM/DD/YYYY):", formatted_date) 


"""
Exercise 3:
Using the strptime function, convert two strings into dates.
Then find the difference in days between the two.
"""

date_str1 = "2024-09-01"  # the first date string
date_str2 = "2024-08-21"  #the second date string

date1 = datetime.strptime(date_str1, "%Y-%m-%d")  #converts the first string to a datetime object
date2 = datetime.strptime(date_str2, "%Y-%m-%d")  #converts the second string to a datetime object

difference = date2 - date1  #find the difference between the two dates as a timedelta object
print(f"Difference in days between {date_str1} and {date_str2}:", difference.days)  


"""
Excercise 4:
Write a program that asks the user for their birthdate and calculates their current 
age using the datetime module.
"""


birthdate_str = input("Enter your birthdate (MM/DD/YYYY): ")  #asks the user to input their birthdate as a string
birthdate = datetime.strptime(birthdate_str, "%m/%d/%Y")  #converts the birthdate string to a datetime object


current_datetime = datetime.now()  # get the current date and time


age_in_years = current_datetime.year - birthdate.year  # subtract the birth year from the current year to get the age


if (current_datetime.month, current_datetime.day) < (birthdate.month, birthdate.day):
    age_in_years -= 1  # if the birthdate hasn't occurred this year yet, subtract 1 year from the age

print("Your current age is:", age_in_years)  # 