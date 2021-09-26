"""
To get rid of the following warning:
```shell
UserWarning: Matplotlib is currently using agg, which is a non-GUI backend, so cannot show the figure.
```

You must have the following installed:
```shell
# Debian
sudo apt-get install python3-tk
# Fedora
sudo dnf install -y python3-tkinker
```

"""
from pathlib import Path
from os import path
from typing import List
from budget import Expense
import matplotlib.pyplot as plt


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

    def __iter__(self):
        """
        Exercise instructions are incomplete, they do not mention to assign self.iter_e = iter(self.expenses).
        > Inside __iter__(), remove pass and replace it with a new iter object with iter() and pass self.expenses
        > into the constructor.
        :return:
        """
        self.iter_e = iter(self.expenses)
        self.iter_o = iter(self.overages)
        return self

    def __next__(self):
        try:
            return self.iter_e.__next__()
        except StopIteration:
            return self.iter_o.__next__()


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

    for entry in myBudgetList:
        print(entry)

    (fig, ax) = plt.subplots()
    labels = ['Expenses', 'Overages', 'Budget']
    values = [myBudgetList.sum_expenses, myBudgetList.sum_overages, myBudgetList.budget]
    ax.bar(labels, values, color=['green', 'red', 'blue'])
    ax.set_title('Your total expenses vs. total budget')
    plt.show()


if __name__ == "__main__":
    main()
