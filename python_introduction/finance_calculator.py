monthly_income = int(input("Enther your monthly income: "))

monthly_expenses = int(input("Enter your total monthly expenses: "))

monthly_savings = monthly_income - monthly_expenses

yearly_savings = monthly_savings * 12

interest = int(yearly_savings * 0.05) # 5% annual interest rate

projected_yearly_savings = yearly_savings + interest

print("Your monthly savings are $" + str(monthly_savings))

print("Projected savings after one year, with interest is, : $" + str(projected_yearly_savings))

