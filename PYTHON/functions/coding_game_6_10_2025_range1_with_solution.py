'''
Write a program that takes two integers, X and N, in one line, separated by a space. Your task is to calculate the sum of all multiples of X up to (and including) the number N.

For example, if X = 3 and N = 10, the multiples of 3 up to 10 are 3, 6, and 9. The sum of these numbers is 18.
Input
A single line containing two integers X and N separated by a space:

X : The base integer to find multiples.
N : The upper limit up to which to sum the multiples.
Output
Output a single integer, which is the sum of all multiples of X from X to N.
Constraints
1 = X = 100
1 = N = 10,000

Example
Input
5 23
Output
50
--------------
71 1077
8520
--------------
2 970
235710
--------------
15 100
315
--------------
8 64
288
--------------
25 100
250
'''
# My solution


x, n = [int(i) for i in input().split()]
print(sum(range(x,n+1,x)))