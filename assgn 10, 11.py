PI = 3.14
radius = float(input("Enter radius: "))

area = PI * (radius ** 2)
print("Area = {0}".format(area))

# 11
income = float(input("Enter salary: "))
expenses = float(input("Enter expenses: "))
savings = income - expenses
percentExpenses = (expenses/ income) * 100
percentSavings = (savings/ income) * 100

print(f"Expenses per month = {percentExpenses: .2f}%")
print(f"Savings per month = {percentSavings: .2f}%")
