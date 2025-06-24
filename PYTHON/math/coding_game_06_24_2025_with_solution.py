'''
Compute the greatest common divisor of |N|to the power of|M| and |M|to the power of|N| where N and M are given integers.

Note: 0 power 0 equals 1
Input
Line 1 : An integer N
Line 2 : An integer M
Output
Line1 : The greatest common divisor of |M|^|N| and |N|^|M|
Constraints
-10= N =10
-10= M = 10
Example
--------------------------------
Input
2
6
Output
4

--------------------------------
Input
-2
-8

Output
64

--------------------------------
Input
-10
5

Output
3125

--------------------------------
Input
-3
-4

Output
1
--------------------------------
'''

def gcd(x,y):
    if x > y:
        the_min = y
        the_max = x
    else:
        the_min = x
        the_max = y
    while not the_min == 0:
        the_min, the_max = the_max % the_min, the_min
    return the_max
        
n = int(input())
m = int(input())

nn = abs(n) ** abs(m)
mm = abs(m) ** abs(n)

print(gcd(nn,mm))


