#Count Vowels
#Ask the user to enter a word and count how many vowels (a, e, i, o, u) are in it.
word = input("Enter a word: ")

vowels = "aeiouAEIOU"
count = 0

for char in word:
    if char in vowels:
        count += 1

print("Number of vowels:", count)