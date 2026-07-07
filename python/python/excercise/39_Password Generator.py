#Password Generator
# Create a program that generates a random 6-character password using letters and digits.

import random
import string

def generate_password(length=6):
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

print("Your password is:", generate_password())