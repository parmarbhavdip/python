'''5) write a program to findout day of week(monday/tuesday/wednesday) from given date.  
    https://www.wikihow.com/Calculate-the-Day-of-the-Week

'''
date=int(input("Enter date (1-31): "))
month=int(input("Enter month (1-12): "))                                    
year=int(input("Enter year (e.g., 2023): "))

if month <3:
     month +=12
     year -=1  
k=year%100
j=year//100
f=(date + (13*(month +1))//5 + k + (k//4) + (j//4) + (5*j)) %7
if f==0:
    print("Saturday")
elif f==1:
     print("Sunday")
elif f==2:
     print("Monday")
elif f==3:
     print("Tuesday")
elif f==4:
     print("Wednesday")
elif f==5:
     print("Thursday")
elif f==6:
     print("Friday")
else:
     print("Invalid date/month/year entered!")

