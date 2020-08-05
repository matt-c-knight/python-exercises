# Import and test 3 of the functions from your functions exercise file.

# Import each function in a different way:

# import the module and refer to the function with the . syntax
# use from to import the function directly
# use from and give the function a different name

import function_exercises as fn
from function_exercises import is_consonant
from function_exercises import handle_commas as hc
fn.is_vowel("a")
fn.is_consonant("n")
hc("1,000")

# How many different ways can you combine the letters 
# from "abc" with the numbers 1, 2, and 3?

# combos = itertools.permutations(list_1, len(list_2))
# print(combos)
# unique = []
# for comb in combos:
#     zipped = zip(comb, list_2)
#     unique.append(list(zipped))
list_1 = ["a","b","c"]
list_2 = [1,2,3]
import itertools
list_3 = list(itertools.product(list_1,list_2))
print(list_3)
print(len(list_3))
# How many different ways can you combine 
# two of the letters from "abcd"?
val = "abcd"
unique = combinations(val, 2)
final = [' '.join(i) for i in unique]
print(final)

perm = list(permutations("abcd", 2))
print(len(perm))

# Total number of users
# Number of active users
# Number of inactive users
# Grand total of balances for all users
# Average balance per user
# User with the lowest balance
# User with the highest balance
# Most common favorite fruit
# Least most common favorite fruit
# Total number of unread messages for all users
import json
from json import load
json.load(profiles.json)
f = open('profiles.json') 
data = json.load(f)
# Total number of users
print(len(data))
# Number of active users
is_true = len([item['isActive'] for item in data if item['isActive' != False])
print(is_true)
# Number of inactive users
is_false = len([item['isActive'] for item in data if item['isActive' == False])

