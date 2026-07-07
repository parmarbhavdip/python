# Write
file = open("test.txt", "w")
file.write("Hello Python")
file.close()

# Read
file = open("test.txt", "r")
print(file.read())
file.close()