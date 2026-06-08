'''
Given the count of integers n and the integers on the following line, move all 0's to the end while maintaining the relative order of the non-zero integers.
Input
Line 1: An integer n that represents the count of the numbers in the next line
Line 2: n integers separated by spaces
Output
The numbers from Line 2 with all the 0's moved to the end while maintaining their relative order.
Constraints
1 ≤ n ≤ 300
-2³¹ ≤ each integer ≤ 2³¹ - 1
Example
Input

5
0 1 0 3 12

Output

1 3 12 0 0

-----------------------
Alternating Zeros

6
0 2 0 1 0 3

2 1 3 0 0 0


-----------------------
Zeros Only

5
0 0 0 0 0

0 0 0 0 0


-----------------------
No Zeros

4
4 5 6 7

4 5 6 7


-----------------------
Negative Integers

20
-639 -97 -676 -283 -201 -887 0 -600 -971 -253 -915 -853 -814 -814 -597 0 -788 -325 -565 -709

-639 -97 -676 -283 -201 -887 -600 -971 -253 -915 -853 -814 -814 -597 -788 -325 -565 -709 0 0


-----------------------
One Integer

1
0

0
-----------------------
Big Integers

10
112912 1293818 19219201 120012 0 92381823 0 0 0 987654321

112912 1293818 19219201 120012 92381823 987654321 0 0 0 0


-----------------------
Lengthy

100
389 0 213 10 406 73 496 463 42 256 221 220 78 339 490 6 368 203 356 114 133 267 462 0 178 180 397 0 441 114 64 399 351 193 0 0 175 155 67 53 187 355 356 176 489 345 455 120 54 214 286 300 91 356 60 81 64 0 118 27 74 103 402 0 389 278 337 111 207 358 221 151 233 235 0 216 180 363 15 425 61 388 60 436 475 131 0 10 289 373 1 210 192 401 0 354 289 339 264 498

389 213 10 406 73 496 463 42 256 221 220 78 339 490 6 368 203 356 114 133 267 462 178 180 397 441 114 64 399 351 193 175 155 67 53 187 355 356 176 489 345 455 120 54 214 286 300 91 356 60 81 64 118 27 74 103 402 389 278 337 111 207 358 221 151 233 235 216 180 363 15 425 61 388 60 436 475 131 10 289 373 1 210 192 401 354 289 339 264 498 0 0 0 0 0 0 0 0 0 0



'''


n = int(input())
non_zero_index = 0
the_result = [0 for x in range(n)]
for i in input().split():
    num = int(i)
    if not num == 0:
        the_result[non_zero_index] = num
        non_zero_index += 1
print(" ".join(str(x) for x in the_result))



'''
# AI solution
n = int(input())
nums = list(map(int, input().split()))

non_zero = [x for x in nums if x != 0]
zeros = [0] * (n - len(non_zero))

result = non_zero + zeros

print(*result)
'''
