'''
You are filming a video where you will offer money to a stranger. They can take it or double it and give it to the next person. But you are given a budget that cant be exceeded and you need to find out how many times it can be doubled
Input
Line 1 an integer startValue,How Much you will Offer to begin with
Line 2 an integer budget,How Much you can spend
Output
an integer How many times it can be doubled
Constraints
0<startValue<100000
startValue≤budget < 1000000000
Example
Input

1
64

Output

6
_________________________________________________



100
100

0

_________________________________________________


10000
500000

5

_________________________________________________

60
121

1
---------------------------------------------
'''

import math
import time

start_value = int(input())
budget = int(input())

