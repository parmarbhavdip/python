''' write a program to figure out whether given number  is composite number or not'''
import sys
number=int(input("enter any number..."))
temp=1
temp<=number

while number % temp==0:
    temp=temp+1
    if number %temp==0:
        print("this number is composite number...")
        sys.exit()
    else:
        print("this number is not composite number ...")
print("good by ")


