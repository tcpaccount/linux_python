'''
In the game Minecraft, many things stack in groups of 64.

here is the structure:
--- |64|64|64(for full stacks)...|(uncompleted piece if it is nonzero)|

Given a number N show how that quantity would look in Minecraft.

For example, if :
N=120 -> |64|56|
N=128 -> |64|64|
N=511 -> |64|64|64|64|64|64|64|63|
...
Input
one integer N
Output
string representing stacked boxes
Constraints
0 < N < 20,000
Example
Input

42

Output

|42|

----------------------------------
test2

126
Output
|64|62|

----------------------------------
test3
1000

Output
|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|40|
----------------------------------
192

Output
|64|64|64|
----------------------------------
10265

Output
|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|64|25|

'''

n = int(input())

counter = n // 64
leftover = n % 64
result = []
if counter > 0:
    result = ["64"]*counter
if leftover > 0:
    result.append(str(leftover))
print("|", "|".join(result), "|", sep="")

