#example of logical operators
d = int(input("Enter number for d==")) 
e = int(input("Enter number for e==")) 
f = int(input("Enter number for f==")) 

# and operator
result = d < e and e < f
print(f"{result} = {d} < {e} and {e} < {f}")

# or operator
result = d < e or e > f
print(f"{result} = {d} < {e} or {e} > {f}")

# not operator
result = not (d < e)
print(f"{result} = not ({d} < {e})")

