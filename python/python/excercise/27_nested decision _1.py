'''write a program to findout heaviest person from 3 person given weight'''

import sys 
person_1=int(input("enter first person weight...."))
person_2=int(input("enter second person weight...."))
person_3=int(input("enter third person weight...."))

if person_1==person_2==person_3:
        print("all person have same  weight!!!")
        sys.exit()
if person_1>person_2:
    print("person 1 have more weight!!!")
else:
    if person_2>person_3:
        print("person 2 have more weight!!!")
    else :
        print("person 3 have more weight!!!")
     