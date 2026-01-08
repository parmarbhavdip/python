'''dictionary
----------------------------
create dictionary to store 20 different detail about your ownself 
print dictionary
print name, age, gender, dob 
add key value pair pincode into dictionary 
add key value pair to store your 5 favourite touriest destination 
print all the favourite touriest destination 

use update method to add new key value pair in dictionary
use update method to change existing key value pair in dictionary
use pop method to remove dob 
use popitem item method to remove last item 

display all keys
display all values 

copy dictionary to another dictionary using copy function 
clear newly create dictionary. '''

# create dictionary to store 20 different detail about your ownself 
student = {'name':'raj sharma','age':21,'weight':51.25,'gender':True,'degree':None,'degree':'BCA','dob':'2/3/2004','address':'bhavnagar','city':'bhavnagr', "state": "Gujarat","mobile": "9102012050",'pincode':364002, "college": "ssccm",'nationality': 'Indian',"occupation": "Software Engineer"}

# print dictionary
print(student)

# print name, age, gender, dob 
print(student['name'])
print(student['age'])
print(student['gender'])
print(student['dob'])

# add key value pair pincode into dictionary 
student.update({'pincode':364520})
print(student)

# add key value pair to store your 5 favourite touriest destination 
student.update({'favourite_touriest_destination':["paris","koriya","london","france"]})
print(student)

# print all the favourite touriest destination 
print(student['favourite_touriest_destination'])

# use update method to add new key value pair in dictionary
student.update({'favourite_touriest_destination':["dubai","koriya","london","france"]})
print(student)

# use pop method to remove dob 
student.pop('dob')
print(student)

# use popitem item method to remove last item 
student.popitem()
print(student)

# display all keys
print(student.keys())

# display all values 
print(student.values())

# copy dictionary to another dictionary using copy function 
student2=student.copy()
print(student2)

# clear newly create dictionary.
student2.clear()

print(student,student2)
