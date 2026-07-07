'''1    -8   27  -64  .....    1000'''

num =int(input("enter a number: "))

while num <=10:
     if num % 2 ==0:
         print(-(num**3), end=' ')
     else:
         print(num**3, end=' ')
     num = num +1
    
print('')    
     