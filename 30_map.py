#example of map function 
numbers = [20,40,50,60,70]

square = map(lambda num: num*num ,numbers)
temp = list(square)
print(temp)

countries = ['India','Russia','China']

countries_lower = map(lambda item: str.lower(item),countries)
print(list(countries_lower))