r'''
You find yourself exploring a place, looking for your grandfather's grave.
Given a particular layout, output your chance to find it with only one try.

The place you're exploring is delimited by symbols -, +, and | as follows:
+--+
| +|
| ||
+--+
As you can see, each grave you'll be able to find inside this area is represented by a + with a | below.
You have to count the graves and give the chance (percentage, rounded) that, if you pick any of them, it will be the one you're looking for.
Input
Line 1 : An integer n, for the graveyard's size.
n next lines : A string representing a line of the graveyard.
Output
Line 1 : Chance (%) to find grandpa's grave directly, rounded.
Constraints
3 < n < 50
Example
Input
5
+---+
|+  |
||  |
|   |
+---+
Output
100%

_________________________________________________________________
6
+----+
|+   |
||  +|
|  +||
|  | |
+----+
33%

_________________________________________________________________

10
+--------+
| ++   + |
| ||  +| |
|+  + |  |
||  |   +|
|  +  + ||
| +|  |  |
|+|+ +++ |
|| | ||| |
+--------+
7%

_________________________________________________________________

12
+----------+
|  o       |
| \|/      |
| / \      |
|          |
|       o  |
|      -|- |
|      / \ |
|  o       |
| /|\      |
| / \      |
+----------+
0%
'''



n = int(input())
the_graveyard = []
for i in range(n):
    line = input()
    the_graveyard.append(list(line))
the_counter = 0
for i in range(1, len(the_graveyard)-2, 1):
    for y in range(1, len(the_graveyard)-1,1):
        if the_graveyard[i][y] == "+" and the_graveyard[i+1][y] == "|":
            the_counter += 1
print(f"{round(100/the_counter)}%") if the_counter > 0 else print("0%")