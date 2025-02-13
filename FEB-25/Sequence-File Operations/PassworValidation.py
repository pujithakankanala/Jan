import re

def is_password_valid(password):
    if (6<= len(password) <=12 and 
        re.search(r"[a-z]", password) and
        re.search(r"[A-Z]", password) and
        re.search(r"[0-9]", password) and
        re.search(r"[$#@]", password)):
        return True
    return False
password= input("Enter the password")
if is_password_valid(password):
    print("Password is valid.")
else:
    print("Password is invalid. It must contain at least one lowercase letter, one uppercase letter, one digit, one special character ($#@), and be between 6 to 12 characters long.")
