import Expense

SPENDING_DATA = "data/spending_data.csv"

expense = Expense.Expenses()
expense.read_expenses(SPENDING_DATA)

spending_categories = []
for expense in expense.list:
    spending_categories.append(expense.category)