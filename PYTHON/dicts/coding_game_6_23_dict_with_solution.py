'''
You are given a hexadecimal number (see note) as a string, and are asked to output the sum of all its digits.

NOTE:
A hexadecimal number (also referred to as base 16) is a number which can have anything in terms of 0-1-2-3-4-5-6-7-8-9-A-B-C-D-E-F as a digit where A=10, B=11, C=12, etc.
Input
First line: You will be given a hexadecimal number as a string (h).
Output
First line: A single number representing the sum of all the digits in h
Constraints
0 < string length of h = 256
Example
Input
123A
Output
16

---------------
FF5D
48
---------------
0123456789ABCDEF
120
---------------
00000000
0
---------------
ABBCCCDDDD1
121
---------------
FFFFFFFFFFFFFFFFFFFFFFFFF
375
---------------
'''

the_dict = dict([(x,y) for x,y in zip("0123456789ABCDEF", range(0,17))])
print(sum([the_dict[x] for x in input()]))

