# Conditional Basics

# prompt the user for a day of the week, print out whether the day is Monday or not
answer = input("What day of week is it?: ")
if answer == "Monday":
    print("Yes, Monday it is!")
else:
    print("It's not Monday today.")
# prompt the user for a day of the week, print out whether the day is a weekday or a weekend
answer_two = input("What day of week is it?: ")
if answer_two == "Monday" or answer_two == "Tuesday" or answer_two == "Wednesday" or answer_two == "Thursday" or answer_two == "Friday":
    print("It's a weekday.")
else:
    print("It's the weekend!")
# create variables and make up values for
# the number of hours worked in one week
hours_worked = int(input("How many hours did you work?: "))
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
    

#    For Loops

# Write some code that prompts the user for a number, 
# then shows a multiplication table up through 10 for that number.
user_input = int(input("Please provide a number between one and ten: "))

for num in range(1,11):
    print(user_input * num)

# For example, if the user enters 7, your program should output:

# Create a for loop that uses print to create the output shown below.

# 1
# 22
# 333
# 4444
# 55555
# 666666
# 7777777
# 88888888
# 999999999

for x in range(1,10): 
    print(str(x)*x)
    
# Prompt the user for an odd number between 1 and 50. 
# Use a loop and a break statement to continue prompting the user if they enter invalid input. 
# (Hint: use the isdigit method on strings to determine this). 
# Use a loop and the continue statement to output all the odd numbers between 1 and 50, 
# except for the number the user entered.



odd_number = input("Enter an odd number between 1 and 50: ")
input_val = True
while(input):
    if odd_number.isdigit() and int(odd_number) % 2 == 1:
        break
    else:
        odd_number = input("Please enter an odd number")
odd_number = int(odd_number)
for num in range(1,50):
    if num % 2 == 0 or num == odd_number:
        continue  
    print(f"Here is the odd number: {num}")  

positive_int = int(input("Please enter a positive integer: "))

while positive_int > 0:
    print(positive_int)
    positive_int -= 1


# Fizzbuzz

# One of the most common interview questions for entry-level programmers is the FizzBuzz test. Developed by Imran Ghory, the test is designed to test basic looping and conditional logic skills.
# Write a program that prints the numbers from 1 to 100.
# For multiples of three print "Fizz" instead of the number
# For the multiples of five print "Buzz".
# For numbers which are multiples of both three and five print "FizzBuzz".

for fizz in range(101):
    if fizz % 3 == 0 and fizz % 5 == 0:
        print("fizzbuzz")
        continue
    elif fizz % 3 == 0:
        print("fizz")
        continue
    elif fizz % 5 == 0:
        print("buzz")
        continue
    

# Display a table of powers.

# Prompt the user to enter an integer.
# Display a table of squares and cubes from 1 to the value entered.
# Ask if the user wants to continue.
# Assume that the user will enter valid data.
# Only continue if the user agrees to.


def question_four():
    numbers = []
    squares = []
    cubes = []
    start = 1 
    input_val = int(input("Please enter an integer: "))
    for count in range (start, input_val + 1) :
        numbers.append(count)
        squares.append(count**2)
        cubes.append(count**3)
    print(numbers)
    print(squares)
    print(cubes)
    cont = input("Would you like to continue: yes or no?: ")
    if cont == "yes":
        question_four()
    

question_four()




# Convert given number grades into letter grades.

# Prompt the user for a numerical grade from 0 to 100.
# Display the corresponding letter grade.
# Prompt the user to continue.
# Assume that the user will enter valid integers for the grades.
# The application should only continue if the user agrees to.
# Grade Ranges:
def grade_checker():
    num_grade = int(input("Please provide your grade between 0 and 100: "))
    if num_grade > 87:
        print("You received an A")
        grade_checker()
    elif num_grade > 79:
        print("You received a B")
        grade_checker()
    elif num_grade > 66:
        print("You received a C")
        grade_checker()
    elif num_grade > 59:
        print("You received a D")
        grade_checker()
    elif num_grade < 60:
        print("You received an F")
        grade_checker()
   

grade_checker()


# Create a list of dictionaries where each dictionary represents a book that you have read. 
# Each dictionary in the list should have the keys title, author, and genre.
# Loop through the list and print out information about each book.

# Prompt the user to enter a genre, then loop through your books list and 
# print out the titles of all the books in that genre.

books = [
    {"title": "Statistics for Absolute Beginners",
    "author": "O Theobald",
    "genre": "Math/Stats" },
    {"title": "A Smarter Way to Learn Javascript",
    "author": "Mark Myers",
    "genre": "Computers"},
    {"title": "Managerial Accounting for Dummies",
    "author": "Mark Holtzman",
    "genre": "Business/Accounting"}
]

for book in books:
    print(book)

book_genre = input("Please enter a genre: Math/Stats, Computers, or Business/Accounting: ")

for book in books:
    if book["genre"] == book_genre:
        print(book["title"])

# ---------------------------------------
# Ryan's walkthrough notes
# day_of_week.lower()
# if day_of_week.lower() in ['saturday', 'sunday']
    # print(f'{day_of_week}')
while True:
    user_number = input("Please provide a number bewteen 1 and 50: ")
    
    if user_number.isdigit():
        user_number = int(user_number)

        large_enough = user_number > 1
        small_enough = user_number < 50
        odd = user_number % 2 != 0

        if large_enough and small_enough and odd:
            break
        else:
            print("Must be less than 50 and greater than 1.")
    else: 
        print("Your input must be numerals.")

user_number

# for i in range(1,50,2):
#     if i == user_number:
#         print("Yikes!")
#         continue
#     print(f"Here is an odd number: {1}")

# while True:
#     user_number = input("Please input a positive integer:")

#     if (user_number.isdigit() anbd
    
#         float(user_number) == int(user_number) and
#         int(user_number > 0):

#         user_number = int(user_number)

#         break
#     else: 
#         print("Your input must be numeric, positive integer value.")

# user_number

# for i in range(1, 101):
#     if i % 3 == 0 and i % 5 == 0:
#         print("Fizzbuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)

# user_number = int(input("Please input an integer: "))

# print("Here is your table!")

# print("number | squared | cubed")
# print("-------|---------|------")
# for i in range(1, user_number +1):
#     print(f"{1}   |  {i**2}  |  {i **3}")

# wants_to_continue = input("Press Y or yes to continue...")


