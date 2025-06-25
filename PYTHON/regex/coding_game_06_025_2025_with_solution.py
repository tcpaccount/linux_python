'''
Find each occurrence of word the in the input string, case insensitive, and count them.
The word the has to be its own word, and not a part of another word: e.g. 'furthermore' doesn't count.
Input
The input is a string of plain text English containing, among others, the word the.
Output
Number of occurrences of the word the in the string given as input
Constraints
0 < length of input < 1024
Example

Input
The goal of this challenge is to find a particular word.

Output
1
--------------------------------------
Input
Hello there, what are the news today?

Output
1
--------------------------------------
Input
Make sure that the first character of actual line content lies on a tab stop, so that the alignment of tabs looks normal.

Output
2
--------------------------------------
Input
Select only those lines containing matches that form whole words. The test is that the matching substring must either be at the beginning of the line, or preceded by a non-word constituent character. Similarly, it must be either at the end of the line or followed by a non-word constituent character.

Output
6
--------------------------------------

'''

import re

print(len(re.findall(r'\bthe\b', input(), re.I)))


