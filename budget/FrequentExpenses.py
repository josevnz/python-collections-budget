import collections
from pathlib import Path
from os import path
from budget import Expense
import matplotlib.pyplot as plt

PARENT_DIR = Path(__file__).parent.parent
SPENDING_DATA = path.join(PARENT_DIR, 'data', 'spending_data.csv')

expenses = Expense.Expenses()
expenses.read_expenses(SPENDING_DATA)

spending_categories = []
for expenses in expenses.list:
    spending_categories.append(expenses.category)
spending_counter = collections.Counter(spending_categories)
print(spending_counter)
top5 = spending_counter.most_common(5)
print(f"Most frequent: {top5}")
(fig, ax) = plt.subplots()
(categories, count) = zip(*top5)
ax.bar(categories, count)
ax.set_title('# of Purchases by Category')
plt.show()
