# Keep asking until correct login

while True:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == "admin" and password == "1234":
        print("Login successful")
        break
    else:
        print("Try again")
