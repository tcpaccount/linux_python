'''
A triple fibonacci is basically fibonacci but the next sequence is the sum of the previous 3 numbers
1, 1, 1, 3, 5, 9...
The sequence starts with index 0
Input
The index of the triple fibonacci sequence
Output
The number from the triple fibonacci sequence
Constraints
0<=index<=50
Example

Input
3

Output
3
----------------------------------------------------------
Test 2
10

Output
193
----------------------------------------------------------
Test 3
20

Output
85525
----------------------------------------------------------
Test 4
50

Output
7440059097409
----------------------------------------------------------

'''

index = int(input())
initial_seq = [1,1,1]

for i in range(index - 3 + 1):
    temp = sum(initial_seq[-3:])
    initial_seq.append(temp)

print(initial_seq[-1])