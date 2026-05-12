expenses = [25, 56.6, 78.9, 12.5, 34.0, 99.78, 45.6]

total_expenses = sum(expenses)
average_expense = total_expenses / len(expenses)
min_expense = min(expenses)
max_expense = max(expenses)

result = (min_expense, max_expense, total_expenses)

print("Total Expenses:", result)