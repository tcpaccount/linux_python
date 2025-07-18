'''
You must output the n-th element of the number sequence, which is specified by these rules:
1. First two elements (N1 and N2) are given.
2. The element with index n is the sum of two previous elements. For example, N4 = N3 + N2.

Example
Input:
0 1
3

Sequence:
0 1 1 2 3 5 8 ...

Output (3rd element):
1
Input
Line 1: First two elements (N1, N2) of the sequence
Line 2: Number n
Output
n-th element of the sequence.
Constraints
1 = n = 500
Example
 Third Fibonacci Number
input
0 1
3

output
1
----------------------------------------
 Eighth Lucas Number
input
2 1
8

output
29
----------------------------------------
First Number Given
input
2 1
1

output
2
----------------------------------------
 Thirty-first Number From The Sequence With Seed Values 3 and 5
input
3 5
31

output
5702887
----------------------------------------
 Seed Values 0
input
0 0
274

output
0
----------------------------------------
 Negative numbers in the seed
input
-2 0
28

output
-242786
----------------------------------------

'''

n1, n2 = [int(i) for i in input().split()]
n = int(input())
