import timeit
from pathlib import Path
from os import path

from budget import Expense
import matplotlib.pyplot as plt


def main():
    expenses = Expense.Expenses()
    try:
        # Do this to make the stupid test happy.
        expenses.read_expenses('data/spending_data.csv')
    except IOError:
        # Look for the file in the right directory ...
        PARENT_DIR = Path(__file__).parent.parent
        SPENDING_DATA = path.join(PARENT_DIR, 'data', 'spending_data.csv')
        expenses.read_expenses(SPENDING_DATA)
    """
    Simple equality test
    """
    divided_for_loop = expenses.categorize_for_loop()
    divided_set_comp = expenses.categorize_set_comprehension()
    if not divided_for_loop == divided_set_comp:
        print('Sets are NOT equal by == test')
    """
    assert divided_for_loop[0] == divided_set_comp[0]
    assert divided_for_loop[1] == divided_set_comp[1]
    assert divided_for_loop[2] == divided_set_comp[2]
    """
    for a, b in zip(divided_for_loop, divided_set_comp):
        if not (a.issubset(b) and b.issubset(a)):
            print("Sets are NOT equal by subset test")
    print(timeit.timeit(
        stmt="expenses.categorize_for_loop()",
        setup='''
from budget import Expense        
expenses = Expense.Expenses()
PARENT_DIR = Path(__file__).parent.parent
SPENDING_DATA = path.join(PARENT_DIR, 'data', 'spending_data.csv')
expenses.read_expenses(SPENDING_DATA)        
''',
        number=1000,
        globals=globals()
    ))


if __name__ == "__main__":
    main()
