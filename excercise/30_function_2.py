# Function to calculate Simple Interest
def simple_interest(p, r, t):
    si = (p * r * t) / 100
    return si

# Taking input from user
principal = float(input("Enter Principal Amount: "))
rate = float(input("Enter Rate of Interest: "))
time = float(input("Enter Time (in years): "))

# Calling function
result = simple_interest(principal, rate, time)

# Display result
print("Simple Interest is:", result)