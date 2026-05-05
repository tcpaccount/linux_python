'''
Given a list of non-negative integers separated by a space print the concatenation of odd numbers such that

If the integer is even get the next odd number
If the integer is odd keep it
Input
A single line containing non-negative integers separated by a space.
Output
A single line of the concatenated odd integers based on the rules.
Constraints
Integers are between 0 (inclusive) and 100 (exclusive).
Example
Input

1

Output

1
---------------------
Test 2

2 4 6 8

3579

----------------------
Test 3

0 0 0 0 0

11111
-----------------------
Test 4

35 35 35 35 35

3535353535

-----------------------
Test 5

98 59 98 82 59 54 71 90 54 92

99599983595571915593


'''

n = input()
print("".join([str(x) if int(x) % 2 else str(int(x) + 1) for x in n.split()]))
