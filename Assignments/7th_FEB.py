'''7th Feb

Create a strong code for password authentication using python.
'''
import re

# Function to check password strength
def check_password_strength(password):
    if len(password) < 8:
        return "Password must be at least 8 characters long"

    if not re.search("[A-Z]", password):
        return "Password must contain at least one uppercase letter"

    if not re.search("[a-z]", password):
        return "Password must contain at least one lowercase letter"

    if not re.search("[0-9]", password):
        return "Password must contain at least one number"

    if not re.search("[@#$%^&*!]", password):
        return "Password must contain at least one special character"

    return "Strong"

# Registration
print("=== Create Password ===")
password = input("Enter a new password: ")

strength = check_password_strength(password)

if strength == "Strong":
    print("Password created successfully!\n")

    # Login authentication
    print("=== Login ===")
    login = input("Enter your password: ")

    if login == password:
        print("Login Successful!")
    else:
        print("Incorrect Password!")
else:
    print("Weak Password:", strength)