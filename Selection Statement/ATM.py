# ATM Withdrawal System

balance = 5000  # Initial balance

amount = float(input("Enter withdrawal amount: "))

# Check if sufficient balance is available
if amount <= balance:
    balance = balance - amount
    print("Transaction successful")
    print("Remaining balance:", balance)
else:
    print("Insufficient balance")
