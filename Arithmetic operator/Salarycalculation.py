# Salary calculation with bonus and deduction

basic_salary = float(input("Enter basic salary: "))

bonus = basic_salary * 0.10       # 10% bonus
deduction = basic_salary * 0.05   # 5% deduction

net_salary = basic_salary + bonus - deduction

print("Bonus:", bonus)
print("Deduction:", deduction)
print("Net Salary:", net_salary)
