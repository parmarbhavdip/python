#write a program to convert given 3 digit amount into words
# input : 175 output : one hundred seventy five  

number= int(input("Enter a 3 digit number: "))

first=number // 100
second=(number // 10) % 10
last=number % 10

words1= ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
words2 = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
words3= ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]


print(words1[first],"hunderad",words2[second],words3[last])
