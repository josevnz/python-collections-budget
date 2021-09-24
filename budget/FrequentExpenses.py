import collections
from pathlib import Path
from os import path
import Expense

PARENT_DIR = Path(__file__).parent.parent
SPENDING_DATA = path.join(PARENT_DIR, 'data', 'spending_data.csv')

expense = Expense.Expenses()
expense.read_expenses(SPENDING_DATA)

spending_categories = []
for expense in expense.list:
    spending_categories.append(expense.category)
spending_counter = collections.Counter(spending_categories)
print(spending_counter)
