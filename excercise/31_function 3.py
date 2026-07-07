# write a program that return current Date
from datetime import date

def get_current_date():
    today = date.today()
    return today

print("Current Date:", get_current_date())

# anothar to 
from datetime import datetime

def get_current_date_formatted():
    now = datetime.now()
    return now.strftime("%A, %d %B %Y")

print("Today is:", get_current_date_formatted())