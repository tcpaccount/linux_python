'''
The program:
Your program must determine in which category belongs a given integer. The possible integers are named intervals that are also given.
The intervals do not overlap.
The integer always belongs to a category.

INPUT:
Line 1: X the integer to categorize.
Line 2: N an integer for the number of categories.
Next N lines: Two integers F and T for the inclusive bounds of the interval, followed by a word category, its name.

OUTPUT:
The name of the category with the interval that contains X.

CONSTRAINTS:
0 < N < 100
-1000 = F = T = 1000
F = X = T

INITIAL CODE(START):
x = int(input())
n = int(input())
the_ranges = {}
for i in range(n):
    inputs = input()
INITIAL CODE(END):

EXAMPLE:
Input
10
3
-1000 -1 negative
0 0 null
1 1000 positive
Output
positive

__________________________
0
3
-1000 -1 negative
0 0 null
1 1000 positive
null
__________________________
81
3
0 21 young
22 59 adult
60 81 elder
elder
__________________________
27
3
0 21 young
22 59 adult
60 81 elder
adult
__________________________
654
5
-500 -65 A
-64 21 B
22 369 C
370 559 D
560 999 E
E
__________________________
0
5
-500 -65 A
-64 21 B
22 369 C
370 559 D
560 999 E
B
__________________________


# My Solution
________


'''

x = int(input())
n = int(input())
the_ranges = {}
for i in range(n):
    inputs = input()


