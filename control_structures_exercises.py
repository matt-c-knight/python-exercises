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


# Create an integer variable i with a value of 5.
i = 5
# Create a while loop that runs so long as i is less than or equal to 15
# Each loop iteration, output the current value of i, then increment i by one.

while i <= 15:
    print(i)
    i += 1

# Create a while loop that will count by 2's starting with 0 and ending at 100. 
n = 0
while n < 100:
    print(n)
    n += 2
# Follow each number with a new line.
# Alter your loop count backwards by 5's from 100 to -10.
x = 100
while x > -15:
    print(x)
    x -= 5
# Create a while loop that starts at 2, and displays the number squared on each line while the number is less than 1,000,000. 
y = 2
while y < 1000000:
    print(y)
    y *= y
    

   For Loops

# Write some code that prompts the user for a number, 
# then shows a multiplication table up through 10 for that number.
user_input = int(input("Please provide a number between one and ten"))

for num in range(1,11):
    print(user_input * num)

# For example, if the user enters 7, your program should output: