# Calculate total bill including GST

amount = float(input("Enter total purchase amount: "))
gst_rate = 18  # 18% GST

# Calculate GST and final amount
gst = (amount * gst_rate) / 100
total_bill = amount + gst

print("GST Amount:", gst)
print("Total Bill:", total_bill)
