'''write a program to accept 2 number from user. and accept choice for operations.
operations will be addition, subtraction, multiplication, division
do operation and display result as per user choice about operation using if elif else statements.'''
number1=float(input("Enter value of number1 :"))
number2=float(input("Enter value of number2 :"))

choice=int(input("Enter choice :"))
if choice ==1:
    Addition = number1 + number2
    print("Addition is:" ,Addition)
elif choice ==2:
    substraction = number1 - number2
    print("substraction is:",substraction)
elif choice ==3:
    Multiplication = number1 * number2
    print("Multiplication is:",Multiplication)
elif choice==4 :
    Division = number1 / number2
    print("Division is:",Division)
else :
    print("Enter invalid choice !!!")