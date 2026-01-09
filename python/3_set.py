destinations= {"Goa", "Manali", "Jaipur", "Agra", "Kerala", "Ladakh","Darjeeling","Udaipur", "Rishikesh", "Varanasi"}
print(destinations)

destinations.add('Gujrat')
destinations.remove('Goa')
print(destinations)

colors = [ "Red","Blue","Green","Yellow","Orange","Purple","Pink","Black","White","Brown"]
print(colors)

unique_colors_set = set(colors) 
print(unique_colors_set)

# union,intersection,difference
set1={10,50,60,40,70,100}
set2={15,20,25,30,60,50}

union=set1.union(set2)
intetsection=set1.intersection(set2)
difference=set1.difference(set2)

print("union",union)
print("inintetsection",intetsection)
print("difference",difference)