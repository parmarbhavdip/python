# write a program that will calculate and display sum of even value into list. user will pass list as argument in function. 

nums = list(map(int, input("Enter numbers: ").split()))

def sum_even(lst):
    return sum(num for num in lst if num % 2 == 0)

print("Sum of even numbers is:", sum_even(nums))
