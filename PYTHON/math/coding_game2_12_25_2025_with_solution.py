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

time1 = time.time()
start_value = int(input())
budget = int(input())

temp1 = (int(math.log((start_value), 2)))
temp2 = (int(math.log((budget), 2)))
time2 = time.time()
print(temp2 - temp1, f"Time Taken For my code: {time2 - time1}")

time1 = time.time()
count = 0
start_value2 = start_value
budget2 = budget

while start_value2 * 2 <= budget2:
    start_value2 = start_value2 * 2
    count = count + 1

print(count, f"Time taken for chatgpt code : {time.time() - time1}")
