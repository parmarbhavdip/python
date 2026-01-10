'''write a program to display dinominations of currency for given amount
input : 887 Rupees 
output : 
500 x 1 = 500
200 x 1 = 200
100 x 1 = 100
50 x 1 =  50
20 x 1 =  20
10 x 1 =  10
5 x 1 =   05
2 x 1 =   02
1 x 1 =   01'''

amount =int(input("Enter amount in rupees: "))

five_h =amount // 500
amount = amount - (five_h * 500)

two_h = amount // 200
amount = amount- (two_h * 200)

hun = amount // 100
amount = amount - (hun*100)

fifty = amount // 50
amount = amount - (fifty*50)

twenty =amount// 20
amount = amount - (twenty*20)

ten = amount// 10
amount = amount - (ten*10)

five = amount // 5
amount = amount - (five*5)

two = amount // 2
amount = amount - (two*2)

one = amount // 1

print("dinominations of currency"\
      "\n 500 *",five_h,"=",500*five_h,\
      "\n 200 *",two_h,"=",200*two_h,\
      "\n 100 *",hun,"=",100*hun,\
      "\n 50  *",fifty,"=",50*fifty,\
      "\n 20  *",twenty,"=",20*twenty,\
      "\n 10  *",ten,"=",10*ten,\
      "\n 05  *",five,"=",5*five,\
      "\n 02  *",two,"=",2*two,\
      "\n 01  *",one,"=",1*one)

