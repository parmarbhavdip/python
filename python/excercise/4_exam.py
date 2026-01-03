#write a prgram to find out simple interest of given amount rate and year
amount=0
rate=0
year=0

amount=input("Enter amount=")
rate=input("Enter rate=")
year=input("Enter year=")

amount=float(amount)
rate=float(rate)
year=int(year)

si=amount*rate*year/100

print("simple interest is",si)