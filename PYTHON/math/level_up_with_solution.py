'''
CodinGame.com is an online platform for programmers to improve their coding skills through game-based challenges and puzzles.

The site has a "leveling" system – by doing various activities you gain XP and once you get enough XP you get promoted to the next level. Specifically, to get from level L - 1 to level L you need (rounded down)
(L ^ 1.5) * 10 XP

For example, to go from level 2 to level 3 you need
3^1.5*10 = 51.96152423 ≈ 51 additional XP.

Your task is to implement the algorithm that determines how much more XP a player needs to level up.
Input
Line 1: An integer level for the level the user is currently on.
Line 2: An integer xp for the amount of XP the user has collected since reaching level
Output
The amount of XP the user has to gain to reach the next level (as an integer),
or LEVEL UP if the user already has enough XP to level up
or X LEVELX UP if the user already has enough XP for a few levels up

Constraints
1 ≤ level ≤ 100
0 ≤ XP ≤ 10000

Initial code(start):
import math

level = int(input())
xp = int(input())

Example
Input

2
0

Output

51


______________________
Input
3
79

Output
1

________________________
Input
6
185

Output
LEVEL UP

________________________
Input
2
131

Output
2 LEVELS UP
_________________________
Input
2
51

Output
LEVEL UP

_____________________
Input
6
200

Output
LEVEL UP

____________________
Input
100
5927

Output
4223

_____________________
Input
10
10000

Output
13 LEVELS UP

'''


import math

level = int(input())
xp = int(input())

levels_up = 0
needed = math.trunc((level + 1) ** 1.5 * 10)

if needed > xp:
    print(needed - xp)
else:
    while needed <= xp:
        levels_up +=1
        level += 1
        xp -= needed
        needed = math.trunc((level + 1) ** 1.5 * 10)
    print("LEVEL UP") if levels_up == 1 else print(f"{levels_up} LEVELS UP")














