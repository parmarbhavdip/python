'''
create tuple to store all states name of india 
display tuple 
display 1st five items 
display 2nd and 3rd and 4th item 
display all items from 7th position onwards 
try to remove 3rd item see what happens 
'''

# create tuple to store all states name of india 
states = ("Andhra Pradesh","Arunachal Pradesh","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal")

# display tuple 
print(states)

# display 1st five items 
print(states[0:5])

# display 2nd and 3rd and 4th item 
print(states[2:5])

# display all items from 7th position onwards 
print(states[6:])

#try to remove 3rd item see what happens 
states.remove("Bihar") 
print(states)