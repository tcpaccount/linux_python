'''
You are given an integer n and a one-dimensional list of L integers (where L is a multiple of n). Reshape this list into a two-dimensional matrix with n rows (and L/n columns), preserving the original element order, and print the result.
Input
Line 1: An integer n – the number of rows.
Line 2: A sequence of space-separated integers – the elements of the 1-D list.
Output
n lines:
On each line, print the next elements of the reshaped matrix, separated by a single space.
Constraints
1 ≤ n ≤ 15

1 ≤ length of L ≤ 100

The length of L is divisible by n.

Each integer in the list fits in a signed 32-bit range.
Example
Input
3
1 2 3 4 5 6
Output
1 2
3 4
5 6

____________________________
Input
4
1 2 3 4 5 6 7 8 9 10 11 12

Output
1 2 3
4 5 6
7 8 9
10 11 12
____________________________
Input
1
1 3 4 6 8 0 8 6 4

Output
1 3 4 6 8 0 8 6 4
____________________________
Input
15
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15

Output
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
____________________________
Input
12
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96

Output
1 2 3 4 5 6 7 8
9 10 11 12 13 14 15 16
17 18 19 20 21 22 23 24
25 26 27 28 29 30 31 32
33 34 35 36 37 38 39 40
41 42 43 44 45 46 47 48
49 50 51 52 53 54 55 56
57 58 59 60 61 62 63 64
65 66 67 68 69 70 71 72
73 74 75 76 77 78 79 80
81 82 83 84 85 86 87 88
89 90 91 92 93 94 95 96
____________________________
Input
1
1

Output
1


'''

n = int(input())
data = input().split()

l = len(data) // n

for i in range(n):
    print(*data[i*l:i*l+l])
