# Calculate bill for multiple users

n = int(input("Enter number of users: "))

for i in range(n):
    units = int(input(f"Enter units for user {i+1}: "))

    if units <= 100:
        bill = units * 2
    else:
        bill = units * 5

    print(f"User {i+1} Bill:", bill)
