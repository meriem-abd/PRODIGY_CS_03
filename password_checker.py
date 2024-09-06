import re

def check(password):
    # Check if the password length is at least 8 characters
    length = len(password) >= 8

    # Check if the password contains at least one lowercase letter
    lower = re.search(r'[a-z]', password) is not None

    # Check if the password contains at least one uppercase letter
    upper = re.search(r'[A-Z]', password) is not None

    # Check if the password contains at least one number
    numbers = re.search(r'\d+', password) is not None

    # Check if the password contains at least one special character
    special = re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None

    # List of criteria results
    criteria = [length, lower, upper, numbers, special]

    # Calculate the strength of the password based on the number of criteria met
    strength = sum(criteria)

    # Determine the strength of the password and print the appropriate message
    if strength == 5:
        print("Very strong password")
    elif strength == 4:
        print("Strong password")
    elif strength == 3:
        print("Moderate password")
    elif strength == 2:
        print("Weak password")
    else:
        print("Very weak password")

    # Provide specific feedback for each criterion not met
    if not length:
        print("Password must be at least 8 characters long.")
    if not lower:
        print("Password must contain at least one lowercase letter.")
    if not upper:
        print("Password must contain at least one uppercase letter.")
    if not numbers:
        print("Password must contain at least one number.")
    if not special:
        print("Password must contain at least one special character.")

# Prompt the user to enter their password
password = input("Enter your password: ")
# Check the password and provide feedback
check(password)

