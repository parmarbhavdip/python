'''if else if decision making 
1) Write a program that takes a 5 subject marks from user. calculate total and Percentage  and prints the grade using the following conditions:

| Percentage | Grade |
| ---------- | ----- |
| 90-100     | A+    |
| 80-89      | A     |
| 70-79      | B     |
| 60-69      | C     |
| 50-59      | D     |
| below 50   | Need to improve  |'''
sub1=float(input("enter marks for subject 1 =="))
sub2=float(input("enter marks for subject 2 =="))
sub3=float(input("enter marks for subject 3 =="))
sub4=float(input("enter marks for subject 4 =="))
sub5=float(input("enter marks for subject 5 =="))

total_marks=sub1+sub2+sub3+sub4+sub5
percentage=(total_marks/500)*100

print("total marks obtained =",total_marks)
print("percentage obtained =",percentage)

if percentage>=90 and percentage<=100:
    print("Grade A+")
elif percentage>=80 and percentage<90:
     print("Grade A")
elif percentage>=70 and percentage<80:
     print("Grade B")
elif percentage>=60 and percentage<70:
     print("Grade C")
elif percentage>=50 and percentage<60:
     print("Grade D")
else:
     print("Need to improve")
print("thank you for using our grading system")
print("have a nice day")


