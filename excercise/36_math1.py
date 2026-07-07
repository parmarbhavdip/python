import math

num = float(input("Enter a positive number: "))

# Convert to positive using fabs
num = math.fabs(num)

# Convert to integer (factorial needs integer)
num = int(num)

# Calculate factorial
result = math.factorial(num)

print("Factorial =", result)