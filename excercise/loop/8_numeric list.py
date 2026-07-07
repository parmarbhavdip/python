''' write a program to count odd and even number in numeric list '''

num_list=[10,23,45,66,60,20,55,33,78,90]

odd_count=0
even_count=0

for num in num_list:
     if num % 2==0:
          even_count+=1
     else:
          odd_count+=1
          
print("total even number is :",even_count)
print("total odd number is :",odd_count)
