# Login Authentication System

username = input("Enter username: ")
password = input("Enter password: ")

# Check login credentials
if username == "admin" and password == "1234":
    print("Login successful")
else:
    print("Invalid credentials")
