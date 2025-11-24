'''
A tiger decided to visit his friend.
It turned out that the tiger's house is located at point 0 and his friend's house is located at point x(x?>?0) of the coordinate line.
In one step the tiger can move 1, 2, 3, 4 or 5 positions forward.
Determine, what is the minimum number of steps he need to make in order to get to his friend's house.

Input
The first line of the input contains an integer x — The coordinate of the friend's house.

Output
Print the minimum number of steps that tiger needs to make to get from point 0 to point x.

Constraints
1=x=1000000

Example

Input

4

Output
1
-------------------------------

12

output
3
-------------------------------

100

output

20
-------------------------------

1000000

output

200000
'''


x = int(input())

steps = [5,4,3,2,1]
counter = 0
for step in steps:
        if x >= step:
            counter += x // step
            x = x % step
            if x == 0:
                break
print(counter)