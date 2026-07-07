# write a program that return current Time
from datetime import datetime

def get_time_12hr():
    now = datetime.now()
    return now.strftime ("%I:%M:%S %p")

print("Current Time:", get_time_12hr())