from pathlib import Path
from os import path
from typing import List
from budget import Expense


class BudgetList:

    def __init__(self, budget: float):
        self.budget = budget
        self.sum_expenses: float = 0
        self.expenses: List[float] = []
        self.sum_overages: float = 0
        self.overages: List[float] = []

    def append(self, item: float):
        if self.sum_expenses + item < self.budget:
            self.expenses.append(item)
            self.sum_expenses += item
        else:
            self.overages.append(item)
            self.sum_overages += item

    def __len__(self) -> int:
        return len(self.expenses) + len(self.overages)


def main():
    # myBudgetList not PEP8 ... whatever ...
    myBudgetList = BudgetList(1200)
    expenses = Expense.Expenses()
    try:
        # Do this to make the stupid test happy.
        expenses.read_expenses('data/spending_data.csv')
    except IOError:
        # Look for the file in the right directory ...
        parent_dir = Path(__file__).parent.parent
        spending_data = path.join(parent_dir, 'data', 'spending_data.csv')
        expenses.read_expenses(spending_data)

    for expense in expenses.list:
        myBudgetList.append(expense.amount)
    print(f'The count of all expenses: {len(myBudgetList)}')


if __name__ == "__main__":
    main()
