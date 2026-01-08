'''List
---------------
create a list to store your favourite destination in india
create a list & store 10 different type of values in it 
    print all values 
    print 1st value 
    print last 5 value 
    print 1st five value 
    print list twice using * 
    print item in the list from 2nd to 5th position'''

# create a list to store your favourite destination in india
destination=["Manali","gujrat","Jaipur","Kerala","Ladakh"]

# create a list & store 10 different type of values in it 
values = [3, "hello", 5.14, True, False, [0,1,2], {"name": "bhavdipsinh"}, (3,4), None, "india"]

# print all values 
print(values)

# print 1st value 
print(values[0])

# print last 5 value 
print(values[5:11])

#print 1st five value 
print(values[0:5])

# print list twice using * 
print(values*2)

#print item in the list from 2nd to 5th position
print(values[1:6])

#print destination and values
print(destination+values)