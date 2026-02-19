# Password retry system (3 attempts)

correct_password = "1234"

for attempt in range(3):
    password = input("Enter password: ")

    if password == correct_password:
        print("Access granted")
        break
    else:
        print("Wrong password")

else:
    print("Account locked after 3 attempts")
