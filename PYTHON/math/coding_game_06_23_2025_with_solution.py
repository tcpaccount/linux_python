'''
Find the hypotenuse of a right triangle given the length of the legs. Round to the nearest integer.
Input
Line 1:length of leg_1
Line 2:length of leg_2
Output
length of the hypotenuse
Constraints
1<=leg_1<=25
1<=leg_2<=25
Example
Input
2
3
Output
4

--------------------
Input
6
4
Output
7
--------------------
Input
8
14
Output
16
--------------------
Input
20
14
Output
24
--------------------
'''

leg_1 = int(input())
leg_2 = int(input())
print(round((leg_1 ** 2 + leg_2 ** 2) ** 0.5)
