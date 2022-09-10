# Any time you take an input from a user in python, the input is converted to a string.
# In order to calculate the input numerically, you have to convert it to an int or float first.

# Integer example: Convert European Elevator Floors to US Floors
inp = input('Europe floor?')
usf = int(inp) + 1
print('US floor', usf)

# Float Example: Calculate Pay (NOTE: It's not a good practice to use float for monetary calculations)
hours_worked = input('Enter number of hours worked:')
hours_worked = float(hours_worked)
pay_rate = input('Enter hourly pay rate:')
pay_rate = float(pay_rate)
gross_pay = hours_worked * pay_rate
print('Gross Pay:', gross_pay)
