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