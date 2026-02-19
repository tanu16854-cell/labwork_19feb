# Calculate average of 5 subjects

total = 0

for i in range(5):
    marks = float(input(f"Enter marks of subject {i+1}: "))
    total = total + marks

average = total / 5

print("Total Marks:", total)
print("Average Marks:", average)
