'''
Line 1: d the number of days the event will last
Line 2: m the number of days in the next month
Line 3: a list of m space-separated values a representing attendance for each day next month
Output
The list of the d consecutive days maximizing attendances, separated by a space
If several consecutive d days maximize the attendances, return the earliest d days
Reminder: the month starts at day 1
Constraints
d, m and a are positive integers
0 < d = m
28 = m = 31
Example
Input
3
30
68 54 32 95 23 65 44 90 77 42 18 110 32 67 95 41 51 39 38 50 54 44 92 34 37 94 41 70 71 58
Output
7 8 9

---------------------------------
2
28
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28
27 28
---------------------------------
7
31
84 45 62 18 47 56 21 105 23 65 74 100 95 79 54 14 39 84 56 42 65 36 66 84 95 65 21 45 73 19 85
8 9 10 11 12 13 14
---------------------------------
28
29
97 54 68 54 15 35 69 54 84 75 13 40 84 56 90 94 84 25 62 100 18 94 63 54 11 82 65 98 65
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28
---------------------------------

---------------------------------

---------------------------------

---------------------------------


'''

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

d = int(input())
m = int(input())
the_max = -math.inf
for i in input().split():
    a = int(i)

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print("solution")
