# Create a password randomly generated with the following criteria:
# 1. At least 8 characters
# 2. At least one number
# 3. At least one letter
# 4. At least one special character
# 5. At least one uppercase letter
# 6. At least one lowercase letter


import random
import string
def checkPassword(password):
    if len(password) < 8:
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char.isalpha() for char in password):
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    if not any(char in string.punctuation for char in password):
        return False
    return True

def generatePassword():
    password = ''
    while checkPassword(password) is False:
        password += random.choice(string.ascii_letters + string.digits + string.punctuation)
    return password
print(generatePassword())