# Calculate SI for multiple customers

n = int(input("Enter number of customers: "))

for i in range(n):
    print(f"\nCustomer {i+1}")

    p = float(input("Enter principal: "))
    r = float(input("Enter rate: "))
    t = float(input("Enter time: "))

    si = (p * r * t) / 100

    print("Simple Interest:", si)
