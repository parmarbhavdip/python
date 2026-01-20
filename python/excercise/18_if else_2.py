''''' write a program to find out elder brother from given two brother's age. 
'''

age1 = int(input("Enter the age of the first brother: "))
age2 = int(input("Enter the age of the second brother: "))

if age1 == age2:
    print("Both brothers are of the same age (Twins).")
elif age1 > age2:
    print("The first brother is the elder one.")
else:
    print("The second brother is the elder one.")
    
    print("Comparison complete.")