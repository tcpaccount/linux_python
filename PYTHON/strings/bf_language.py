'''
The Simple BF language consists of three characters and a single 8-bit value in memory.
+ indicates to increment that value.
- decrements it.
. means output the current ASCII value.

This value cannot underflow or overflow.
If the memory value would become negative, value < 0, output UNDERFLOW.
If the memory value would exceed 8-bit, value > 255, output OVERFLOW.
The value starts at 0.
Input
A string only consisting of characters + - .
Output
The output string of the program if the memory stays within bounds.
Otherwise UNDERFLOW or OVERFLOW.
Constraints
0 < input length < 1024
0 <= memory value < 256

Initial code(start):

s = input()

Initial code(end):o

HINT (contracts, functions and techniques that might be useful for solving the problem):
1. Understanding of ASCII/Unicode
2. The chr() function in Python is a built-in function that takes an integer as an argument
 and returns the string representing the character corresponding to that integer's Unicode code point.

Example
Input

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.++++++++++++.-----------.+.-----------------------.

Output

CODE.
----------------Example2-----------------------

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.

output
OVERFLOW

----------------Example3-----------------------

+.--.

UNDERFLOW

----------------Example4-----------------------


+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.---.+++++++++.---------------------------------------...++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.------------------------------------------------------------.-----.+++.--.

SPY222p4/20

----------------Example5-----------------------

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.

d

'''

s = input()