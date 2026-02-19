# Online Shopping Discount System

amount = float(input("Enter purchase amount: "))

# Apply discount based on amount
if amount > 5000:
    discount = amount * 0.20
elif amount > 2000:
    discount = amount * 0.10
else:
    discount = 0

final_price = amount - discount

print("Discount:", discount)
print("Final Price:", final_price)
