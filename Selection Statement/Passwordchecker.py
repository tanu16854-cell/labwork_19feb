# Password Strength Checker

password = input("Enter password: ")

# Check password strength
if len(password) >= 8:
    print("Strong password")
else:
    print("Weak password (must be at least 8 characters)")
