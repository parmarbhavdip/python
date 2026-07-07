#write a program that will find and print maximum number from list, user will pass list as argument in function. 

nums = list(map(int, input("Enter numbers separated by space: ").split()))


def find_max(lst):
    return max(lst)

print("Maximum number is:", find_max(nums))