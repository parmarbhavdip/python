'''write a program to findout most young person from 4 person given age'''
age1 = int(input("Enter age of person 1: "))
age2 = int(input("Enter age of person 2: "))
age3 = int(input("Enter age of person 3: "))
age4 = int(input("Enter age of person 4: "))
if age1 < age2:
     if age1 < age3:
          if age1 < age4:
               print("Person 1 is the youngest")
          else:
               print("Person 4 is the youngest")
     else:
          if age3 < age4:
               print("Person 3 is the youngest")
          else:
               print("Person 4 is the youngest")
else:
     if age2 < age3:
          if age2 < age4:
               print("Person 2 is the youngest")
          else:
               print("Person 4 is the youngest")
     else:
          if age3 < age4:
               print("Person 3 is the youngest")
          else:
               print("Person 4 is the youngest")
               


