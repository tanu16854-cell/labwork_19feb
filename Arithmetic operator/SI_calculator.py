# Simple Interest Calculator using arithmetic operators

principal = float(input("Enter principal amount: "))
rate = float(input("Enter rate of interest: "))
time = float(input("Enter time (in years): "))

# Formula: SI = (P * R * T) / 100
simple_interest = (principal * rate * time) / 100

print("Simple Interest =", simple_interest)
