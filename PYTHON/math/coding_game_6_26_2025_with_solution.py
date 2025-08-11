'''
Given a regular n-gon, find the measures of a single interior angle, a single exterior angle, and if the angles are both odd or even.

The sum of the exterior angles is always 360.

Find the measures of the interior angles using the following formula: (n-2)*180/n
Input
Line 1: a number n for number of sides the polygon has.
Output
Line 1: space-separated integers, interior angle measurei, and exterior angle measuree.
Line 2: output even if both the angle measures are even, otherwise odd
Constraints
0 < n < 40
n is also chosen such that the angles are always integers and don't need any rounding.
Example
Input
3

Output
60 120
even
------------------------
Input
12

Output
150 30
even
------------------------
Input
24

Output
165 15
odd
------------------------
Input
30

Output
168 12
even

'''

n = int(input())

inter =((n-2) * 180) // n
exter = 180 - inter
print(inter, exter)
print("even") if not inter % 2 and not exter % 2 else print("odd")

