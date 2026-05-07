'''
A tautogram is a text in which every word starts with the same letter, ignoring case. Your goal is to check whether the given input text is a tautogram.
Input
Line 1 : A string text containing the text to check.
Output
The uppercase letter that makes the given text a tautogram, or - in case the text is not a tautogram.
Constraints
3 ≤ length of text ≤ 99
text always contains at least two words, separated by a single space.
Each word starts with a letter.
Example
Input

She sells seashells

Output

S
-------------------------------
Test 2

Betty bought a bit of butter

-

-------------------------------
Test 3

Happy hippos are hollow inside

-

-------------------------------
Test 4

truly they triumph, trumpeting trills to trounce the terrible travesties.

T

-------------------------------
Test 5

Clever crocodiles can constantly carry cats

C

-------------------------------

'''

text = input()

the_letter = text[0].lower()

if all([True if x[0].lower() == the_letter else False for x in text.split()]):
    print(the_letter.upper())
else:
    print("-")
