'''
Multyply first digit from the number by the sum of the rest of the digits of the same number

Example1: 
1234

output
9
_________________________________
-1234

output
-9

_________________________________
9

output
0
_________________________________
0

output
0
_________________________________
201

output
2
'''



_input = _original_input = int(input())
the_sum = []

# Using String manipulations
if _original_input < 0:
    print(int(str(_original_input)[:2]) * sum([int(x) for x in str(_original_input)[2:]]))
else:
    print(int(str(_original_input)[:1]) * sum([int(x) for x in str(_original_input)[1:]]))

# Leveraging math
while (new_num := abs(_input) // 10) > 0:
    the_sum.append(abs(_input) % 10)
    _input = new_num
if _original_input < 0:
    print("-", _input * sum(the_sum), sep="")
else:
    print(_input * sum(the_sum))