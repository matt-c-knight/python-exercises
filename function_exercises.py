# Create a file named function_exercises.py for this exercise. 
# After creating each function specified below, write the necessary code in order to test your function.

# Define a function named is_two. 
# It should accept one input and return True if the passed input 
# is either the number or the string 2, False otherwise.
def is_two(x):
    if x == 2 or x == '2':
        return True
    else:
        return False

# assert is_two(2) == True
# Define a function named is_vowel. It should return True if the 
# passed string is a vowel, False otherwise.
def is_vowel(letter):
    letter = letter.lower()
    if letter in ['a', 'e', 'i', 'o', 'u']:
        return True
    else:
        return False

# Define a function named is_consonant. It should return True 
# if the passed string is a consonant, False otherwise. Use your is_vowel 
# function to accomplish this.
def is_consonant(letter):
    if is_vowel(letter) == True:
        return False
    else:
        return True

# Define a function that accepts a string that is a word. 
# The function should capitalize the first letter of the word if
# the word starts with a consonant.
def cap_word(word):
    if is_consonant(word[0]) == True:
        return word.capitalize()
    else:
        return False

# Define a function named calculate_tip. 
# It should accept a tip percentage (a number between 0 and 1) 
# and the bill total, and return the amount to tip.
def calculate_tip(tip,total):
    amount = tip * total
    return round(amount, 2)

calculate_tip(.3, 40)
# Define a function named apply_discount. 
# It should accept a original price, and a discount percentage, 
# and return the price after the discount is applied.
def apply_discount(price,discount):
    discount_amt = price * discount
    total = price - discount_amt
    return total

apply_discount(25,.10)

# Define a function named handle_commas. 
# It should accept a string that is a number that contains commas 
# in it as input, and return a number as output.
def handle_commas(num):
    num_list = list(num)
    for number in num_list:
        if number == ",":
            num_list.remove(number)
    new_list = ''.join(num_list)
    new_list = int(new_list)
    return new_list
    

 
# Define a function named get_letter_grade. 
# It should accept a number and return the letter grade 
# associated with that number (A-F).
def get_letter_grade(num):
    if num > 89:
        return "A"
    elif: num >79:
        return "B"
    elif: num > 69:
        return "C"
    elif: num > 59:
        return "D"
    else:
        return "F"

# Define a function named remove_vowels that accepts a string 
# and returns a string with all the vowels removed.
def remove_vowels(word):
    word = word.lower()
    vowels = ['a', 'e', 'i', 'o', 'u']
    for i in word:
        if i in vowels:
            word = word.replace(i,"")
    return word

# Define a function named normalize_name. It should accept a string and 
# return a valid python identifier, that is:
# anything that is not a valid python identifier should be removed
# leading and trailing whitespace should be removed
# everything should be lowercase
# spaces should be replaced with underscores
# for example:
# Name will become name
# First Name will become first_name
# % Completed will become completed

def normalize_name(word):
    word = word.lower()
    new_word = word.replace(" ", "_")
    new_word = new_word.strip()
    newest_word = new_word.replace("%","")
    if newest_word[0] == "_" or newest_word[:-1] == "_":
        newest_word = newest_word.replace("_","")
    return newest_word

Write a function named cumulative_sum that accepts a list of numbers and returns a list
that is the cumulative sum of the numbers in the list.
cumulative_sum([1, 1, 1]) returns [1, 2, 3]
cumulative_sum([1, 2, 3, 4]) returns [1, 3, 6, 10]

def cumulative_sum(seq):
    new_list = []
    i = 0
    for x in seq:
        i += x
        new_list = new_list.append(i)
    return new_list
