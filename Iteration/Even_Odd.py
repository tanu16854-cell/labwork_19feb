# Count even and odd numbers

even = 0
odd = 0

n = int(input("Enter number of inputs: "))

for i in range(n):
    num = int(input("Enter number: "))

    if num % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even numbers:", even)
print("Odd numbers:", odd)
