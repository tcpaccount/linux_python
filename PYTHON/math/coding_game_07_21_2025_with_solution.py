'''
You are given 2 points, find the distance between them, output the result rounded down.
Input
Line 1: X and Y of the first point.
Line 2: X and Y of the second point.
Output
Line 1: Distance between points.
Constraints
X and Y are positive or negative integers.

-----------------------------
input

8 1
11 5

output
5

-----------------------------
input
1 3
2 4

output
1


-----------------------------
input
15 13
14 8

output
5


'''

x_1, y_1 = [int(i) for i in input().split()]
x_2, y_2 = [int(i) for i in input().split()]

print(int(((x_1 - x_2) ** 2 + (y_1 - y_2) ** 2) ** 0.5))