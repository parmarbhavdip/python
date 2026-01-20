'''''         write a program to accept length and width of two different farm from user. and find out & display which farm is bigger 
'''

length = float(input("enter length of farm 1: "))
width = float(input("enter width of farm 1: "))

length2 = float(input("enter length of farm 2: "))
width2 = float(input("enter width of farm 2: "))

area1 = length * width
area2 = length2 * width2

if area1 > area2:
     print("farm 1 is bigger")

if area2 > area1:
     print("farm 2 is bigger")
     
if area1 == area2:
    print("both farms are equal")