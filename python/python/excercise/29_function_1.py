# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(f):
    celsius = (f - 32) * 5/9
    return celsius

fahrenheit = float(input("Enter temperature in Fahrenheit: "))
result = fahrenheit_to_celsius(fahrenheit)

print("Temperature in Celsius:", result)