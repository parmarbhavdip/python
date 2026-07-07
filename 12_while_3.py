#write a program to findout factorial of given number
#input = 6
#process = 6 x 5 x 4 x 3 x 2 x 1 

num = int(input("enter a number to findout factorial:")) #6
fac=1

while num >=1:
     fac = fac * num  # fac = 1*6 = 6 , fac = 6*5 = 30 , fac = 30*4 = 120
     num = num - 1    # num = 6-1=5 , num = 5-1=4 , num = 4-1=3
     
print("factorial is:",fac)
