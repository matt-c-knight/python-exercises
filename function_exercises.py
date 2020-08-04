Create a file named function_exercises.py for this exercise. 
After creating each function specified below, write the necessary code in order to test your function.

# Define a function named is_two. 
# It should accept one input and return True if the passed input 
# is either the number or the string 2, False otherwise.
def is_two(x):
    if x == 2 or x == '2':
        return True
    else:
        return False

assert is_two(2) == True
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