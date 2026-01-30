''' write a program to figure out whether given number  is composite number or not'''

num = int(input("Enter a number: "))

is_composite = False

for i in range(2, num):
     
    if num % i == 0:
        is_composite = True
        
        break
   
if is_composite:
    print(f"{num} is a composite number.")
    
else:
    print(f"{num} is not a composite number.")
    


