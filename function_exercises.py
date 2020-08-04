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
