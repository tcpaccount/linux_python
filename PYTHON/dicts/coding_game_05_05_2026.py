'''
Aww... Look at your child! They don't know how to write properly yet!

You will be given a digit digit, and two letters old and new.
Your task will be to channel your inner toddler, and spell out digit in English, but replacing all instances of old with new.
If there is no old in the spelling of digit, then you should output its correct spelling.

For reference, here are the expected correct spellings of all digits:
"zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"
Input
Line 1: a digit digit
Line 2: old, new 2 letters separated by a space
Output
A string spelling out digit, with the old letters replaced by new
Constraints
0 <= digit <= 9
Example
Input

5
v f

Output

fife

--------------------------
0
o r

Output
zerr
_________________________--
2
x y

two
--------------------------
4
u o

foor
--------------------------
3
e o

throo

'''

digit = int(input())
old, new = input().split()
