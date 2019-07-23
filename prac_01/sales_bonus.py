"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

sales = float(input("Enter sales: $"))
if sales < 1000:
    calculate = (10/100)*sales
    print(calculate)
else:
    calculate = (15/100)*sales
    print(calculate)