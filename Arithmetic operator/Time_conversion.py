# Convert seconds into hours, minutes, seconds

seconds = int(input("Enter total seconds: "))

hours = seconds // 3600
remaining = seconds % 3600

minutes = remaining // 60
secs = remaining % 60

print("Hours:", hours)
print("Minutes:", minutes)
print("Seconds:", secs)
