# Calculate discount and final price

price = float(input("Enter product price: "))
discount_percent = float(input("Enter discount percentage: "))

discount = (price * discount_percent) / 100
final_price = price - discount

print("Discount Amount:", discount)
print("Final Price:", final_price)
