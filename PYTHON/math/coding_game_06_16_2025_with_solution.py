'''
Line 1: N - amount of numbers.
Next N lines: B - number in binary form.
Output
Sum of numbers that are multiples of 5.
Constraints
2 = N = 5
Example
Input
2
00000101
00001101
Output
5
----------------
Input
3
00001111
00011011
00100011
Output
50
----------------
Input
4
00110010
01001010
01100011
01100100
Output
150
----------------
Input
5
00000101
01100011
10010110
10101110
11111010
Output
405
'''
# My solution

total = 0
n = int(input())
for i in range(n):
    b = int(input(),2)
    if b % 5 == 0:
        total += b
    # above 2 lines of condition can be coded with 1 lines like so
    # total += b if not b % 5 else 0

print(total)
