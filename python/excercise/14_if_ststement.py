''''' if decision making 
        1) write a program to convert 24 hours time into 12 hours format time and display it with AM PM message. 
        input : 15 hours 
        output  3 PM 

        input : 11 hours 
        output  11 AM 

        input : 25 hours 
        output  invalid input '''
import sys
hours = int(input("enter hours in 24 hours format: "))

if  hours <= 12:
  if hours == 12:
      print("12 pm")
      sys.exit()
      print(f"{hours}am")   
 
if hours>12 and hours <=24:
    if hours== 24:
      print("12 pm")
      sys.exit()
      
      hours=hours-12
      print(f"{hours}pm")  
    
    if hours>24:
        print("invalid input") 

      
    


    