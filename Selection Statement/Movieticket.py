# Movie Ticket Pricing System

age = int(input("Enter your age: "))

# Determine ticket price
if age < 12:
    price = 100
elif age <= 60:
    price = 200
else:
    price = 150

print("Ticket price:", price)
