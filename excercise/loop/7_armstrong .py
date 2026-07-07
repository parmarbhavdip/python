'''7) write a program to figure out whether given number  is armstrong number or not'''

number=int(input("enter any number..."))

temp=number
sum=0

while temp>0:
     digit=temp % 10
     sum=sum+digit**3
     temp=temp//10
     
if sum==number:
     print("this number is armstrong number...")
else:
     print("this number is not armstrong number ...")

