# Calculate total price of items

total = 0

n = int(input("Enter number of items: "))

for i in range(n):
    price = float(input(f"Enter price of item {i+1}: "))
    total += price

print("Total amount:", total)
