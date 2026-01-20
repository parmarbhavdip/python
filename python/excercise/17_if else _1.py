'''''write a program to find out whether given year is millennium year or not. using if else decision making statements.
'''
import sys

year = int(input("Enter the year: "))
if year % 1000 == 0:
    print(f"{year} is a millennium year.")
    sys.exit() 
if year % 1000 != 0:
    print(f"{year} is NOT a millennium year.")
else:
     print("Invalid input.")

print('Good bye....')

     