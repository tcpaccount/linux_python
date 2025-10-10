'''
A contribution by KerbalNo15
 Approved by Zmagar,papjimandelie.f.asmar
 	Goal
George is looking for the best value snack food in his local supermarket. He doesn't care about calories; to George all that matters is weight.
Input
Line 1: n The number of snack foods George will be comparing

Next n lines:
String snackName, Integer snackWeight (in kilograms), and Integer snackPrice (in Rai Stones) separated by spaces
Output
The name of the most cost-effective snack food.
Constraints
0 < n < 50
There will never be a tie between any two items
Example
---------------------------
Input
3
Rice_Crackers 2 15
Wonderchocolate 3 20
Doughnuts 2 25

Output
Wonderchocolate
----------------------------
4
Potato_Chips 1 2
Tea 1 6
Coffee_Beans 1 4
Cane_Sugar 12 6

Output
Cane_Sugar
----------------------------
5
Mushrooms 1 12
Apples 6 6
Turkey 1 2
Eggs 5 1
Chicken 2 1

Output
Eggs
----------------------------
4
Maple_Syrup 1 3
Pancake_Batter 2 1
Butter 1 2
Corn 1 1

Output
Pancake_Batter

'''

import sys
import math


current_max = math.inf
current_product = None
n = int(input())
for i in range(n):
    inputs = input().split()
    name = inputs[0]
    quantity = int(inputs[1])
    price = int(inputs[2])
    if price / quantity < current_max:
        current_max = price / quantity
        current_product = name
print(current_product)
