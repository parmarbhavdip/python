''' write a program to figure out whether given number  is perfect number or not'''
 
number=int(input("enter any number..."))

temp=1
sum=0

while temp<number:
     
    if number % temp==0:
        sum=sum+temp
        
    temp=temp+1
if sum==number:
    print("this number is perfect number...")
    
else:
    print("this number is not perfect number ...")
print("good by ")



