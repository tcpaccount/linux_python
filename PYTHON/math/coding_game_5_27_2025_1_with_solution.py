'''
The Multiplicative Persistence:

Giving an integer N in input:
In math, the multiplicative persistence of N is the number of times we can multiply the digits of N together before reaching a single digit number.

For example:
The multiplicative persistence of 679 is 5 because:
679: 6 x 7 x 9 = 378
378: 3 x 7 x 8 = 168
168: 1 x 6 x 8 = 48
48: 4 x 8 = 32
32: 3 x 2 = 6 (one-digit number)
It took 5 steps to get to a one-digit number, so the multiplicative persistence of 679 is 5.

IMPORTANT : ATTEMPT TO SOLVE IT WITHOUT STRING<->INT CASTING CONVERTIONS.

Input
Line 1: An integer N
Output
Line 1 : The multiplicative persistence of N
Constraints
0 = N < 2^63

Initial code(start):
n = int(input())
Initial code(end)

Example
Input
679
Output
5
______________
738
4
______________
877799
6
______________
432089
1
______________
7
0
______________
0
0
______________
277777788888899
11
_______________

'''
# My solution

n = int(input())
the_counter = 0
while n // 10 > 0:
    level = 1
    the_digits = []
    inner_number = n
    while inner_number // 10 > 0:
        the_digits.append(inner_number % 10)
        inner_number //=10
    else:
        the_digits.append(inner_number)
    the_counter += 1
    n = eval("*".join([str(x) for x in the_digits]))
    the_digits.clear()
print(the_counter)

