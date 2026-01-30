''' 0    1   1   2    3   5   8   13  .... 100'''

num_1=0
num_2=1
print(num_1,end=' ')
print(num_2,end=' ')

count=0

while count <10:
     num_next=num_1 + num_2
     print(num_next,end=' ')
     num_1=num_2
     num_2=num_next
     count=count +1
     
print(' ')

 