# Write some Python code, that is, variables and operators, to describe the following scenarios. Do not worry about the real operations to get the values, the goal of these exercises is to understand how real world conditions can be represented with code.

# You have rented some movies for your kids: 
# The little mermaid (for 3 days), 
# Brother Bear (for 5 days, they love it), 
# and Hercules (1 day, you don't know yet if they're going to like it). 
# If price for a movie per day is 3 dollars, how much will you have to pay?

little_mermaid = 3
brother_bear = 5
Hercules = 1

total = (little_mermaid * 3) + (brother_bear * 3) + (Hercules * 3)
total_other = (little_mermaid + brother_bear + Hercules) * 3
print(total)
print(total)

# Suppose you're working as a contractor for 3 companies: 
# Google, Amazon and Facebook, 
# they pay you a different rate per hour. 
# Google pays 400 dollars per hour, Amazon 380, and Facebook 350. 
# How much will you receive in payment for this week? 
# You worked 10 hours for Facebook, 6 hours for Google and 4 hours for Amazon.

google = 400
amazon = 380
facebook = 350

payment = (facebook * 10) + (google * 6) + (amazon * 4)
print(payment)

# A student can be enrolled to a class only if the class is not full 
# and the class schedule does not conflict with her current schedule.


is_not_full = True
is_conflict= False
is_enrolled = is_not_full and not is_conflict

print(is_enrolled)

# A product offer can be applied only if people buys more than 2 items, and the offer has not expired. Premium members do not need to buy a specific amount of products.

bought_more_than_two = True
is_expired = False
is_premium = True
apply_offer = (bought_more_than_two and not is_expired) or is_premium

print(apply_offer)

# Create a variable that holds a boolean value for each of the following conditions:

# the password must be at least 5 characters
# the username must be no more than 20 characters
# the password must not be the same as the username
# bonus neither the username or password can start or end with whitespace
username = 'codeup'
password = 'notastrongpassword'

pass_char = len(password)
user_char = len(username)

is_valid = pass_char > 5 and user_char < 20 

print(is_valid)

# Bonus questions:

fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]

output = [fruit.upper() for fruit in fruits]
# print(output)

capitalized_fruits = [fruit.capitalize() for fruit in fruits]
# print(capitalized_fruits)





def more_than_two_vowels(seq):
    vowels = 'aeiou'
    count = 0
    for i in seq:
        if i in vowels:
            count = count + 1
    return count

fruits_with_more_than_two_vowels = [fruit for fruit in fruits if more_than_two_vowels(fruit) > 2]
print(fruits_with_more_than_two_vowels)

def two_vowels(seq):
    vowels = 'aeiou'
    count = 0
    for i in seq:
        if i in vowels:
            count = count + 1
    return count
fruits_with_two_vowels = [fruit for fruit in fruits if more_than_two_vowels(fruit) == 2]
print(fruits_with_two_vowels)

def char_counter(seq):
    count = 0
    for i in seq:
        count = count + 1
    return count
fruits_with_more_than_five = [fruit for fruit in fruits if char_counter(fruit) > 5]
print(fruits_with_more_than_five)


fruit_length_count = [len(fruit) for fruit in fruits]
print(fruit_length_count)