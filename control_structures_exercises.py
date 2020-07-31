# Conditional Basics

# prompt the user for a day of the week, print out whether the day is Monday or not
answer = input("What day of week is it?")
if answer == "Monday":
    print("Yes, Monday it is!")
else:
    print("It's not Monday today.")
# prompt the user for a day of the week, print out whether the day is a weekday or a weekend
answer_two = input("What day of week is it?")
if answer_two == "Monday" or answer_two == "Tuesday" or answer_two == "Wednesday" or answer_two == "Thursday" or answer_two == "Friday":
    print("It's a weekday.")
else:
    print("It's the weekend!")
# create variables and make up values for
# the number of hours worked in one week
hours_worked = int(input("How many hours did you work?"))
# the hourly rate
rate = 14
# how much the week's paycheck will be
# paycheck = hours_worked * rate
# write the python code that calculates the weekly paycheck. You get paid time and a half if you work more than 40 hours
if hours_worked > 40:
   overtime = hours_worked - 40
   overtime_total = overtime * (rate * 1.5)
   paycheck_total = overtime_total + ((hours_worked - overtime) * rate)
   print(paycheck_total)
else:
   check = hours_worked * rate
   print(check)