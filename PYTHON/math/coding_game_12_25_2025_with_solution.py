'''
Given n integers, find the minimum and maximum values that can be calculated by summing exactly n-1 of the n integers.
Then print the respective minimum and maximum values as a single line of two space-separated long integers.

example

n = 5

arr = [1, 2, 3, 4, 5]

You will need the sum of 4 items.

The minimum sum is 1+2+3+4=10 and the maximum sum is 2+3+4+5=14.

The function will print 10 14
Input
Line 1: An integer N for the number of integers to sum.
Next line: Space separated integers arr to sum.
Output
Line 1 : Space separated minimum sum and maximum sum.
Constraints
2 ≤ N ≤ 100

arr: Space-separated integers -1000 < Each Integer < 100000000
Example
Input

5
1 2 3 4 5

Output

10 14
-----------------------------------
9
1 2 3 5 7 7 3 2 3
Output
26 32

-----------------------------------
6
123 123 425 3456 345234 8273746
Output
349361 8622984

-----------------------------------

2
1 2
Output
1 2
-----------------------------------

3
-1 0 1
Output
-1 1



'''


n = int(input())
arr = input()
my_list = [int(x) for x in arr.split(" ")]
mn = min(my_list)
mx = max(my_list)
print(sum(my_list)-mx, sum(my_list)-mn)

