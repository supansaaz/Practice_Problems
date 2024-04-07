#Expense Tracker
income=float(input("Enter your income "))
print("Enter the expenses ")
food=float(input("Enter expenses for food"))
rent=float(input("Enter expenses for rent"))
other_income=float(input(("Enter the other income")))
total_income=income+other_income
total_expenses=food +rent
remaining_total=total_income-total_expenses
print("The remaining amount is ",remaining_total)

