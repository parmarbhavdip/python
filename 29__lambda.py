#example of lambda function (must be single line and no need of return )

getInterest = lambda amount,rate, year: (amount * rate * year) / 100
getSquare = lambda num: num * num 
getQube = lambda num: getSquare(num) *num

amount = int(input("enter amount"))
rate = int(input("enter rate"))
year=int(input("enter year"))

num =int(input("enter number to get squre and qube"))

print(getInterest(amount,rate,year)) 
print(getSquare(num))
print(getQube(num))

