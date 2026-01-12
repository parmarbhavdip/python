# write a program to convert given minutes into hours and remaining minutes
# input : 150 minutes 
# output : 2 hours and 30 minutes 

minutes=int(input("enter minute and hours="))

hours=minutes // 60
minutes=minutes % 60

print(hours,"hours",minutes,"minutes")

