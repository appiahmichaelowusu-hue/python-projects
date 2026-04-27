monthly_income=int(input("Enter monthly income: $"))
liabilities=[]
costs=[]
for i in range(5):
    expense=input("Enter expense: ")
    cost=int(input("Enter cost: $"))
    liabilities.append(expense)
    costs.append(cost)
total_expenses=sum(costs)
remaining_balance=monthly_income-total_expenses
print(f"Total Expenses: ${total_expenses}")
print(f"Remaining Balance: ${remaining_balance}")
with open("finance report.txt", "a")as file:
    file.write(f"Monthly Income: ${monthly_income}\n")
    for i in range(len(liabilities)):
        file.write(f"{liabilities[i]}: ${costs[i]}\n")
    file.write(f"Total Expenses: ${total_expenses}\n")
    file.write(f"Remaining Balance: ${remaining_balance}\n")
with open("finance report.txt", "r")as file:
        print("Detail of Finance Report:")
        content=file.read()
        print(content)