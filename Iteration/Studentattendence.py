# Count present students

present_count = 0

n = int(input("Enter total students: "))

for i in range(n):
    status = input(f"Student {i+1} (P/A): ")

    if status == "P":
        present_count += 1

print("Total Present:", present_count)
