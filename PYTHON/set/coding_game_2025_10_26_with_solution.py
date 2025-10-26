'''
You are given a string containing 25 different lowercase letters from the English alphabet (a to z) with exactly one missing letter.
Print the missing letter.
Input
One line: A string s of 25 lowercase letters, in any order, with no duplicates.
Output
One line: the missing letter from a to z.
Constraints
Input length is exactly 25.
All characters are lowercase English letters.
Exactly one letter is missing.
Example
Input

qazwsxedcrfvtgbyhnujmikpl

Output
o

______________________
 Test 2

mfukqzjldngyrtesacxovhbpi

Output
w

----------------------
Test 3

xkqtrvjzobmeyhsfpdgwulanc

Output
i

----------------------
Test 4

vnmlkqipxozajydfrhutwbcsg

Output
e

----------------------
'''

import string


s = input()
r = string.ascii_lowercase

try:
    result = next(iter(set(r).difference(set(s))))
    print(result)
except StopIteration:
    print("Error on input data")