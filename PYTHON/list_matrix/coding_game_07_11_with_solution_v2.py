'''
Given a grid of mine locations (where . are empty cells and x are mines), your goal is to display the grid like it appears if you win the game.
Each position is a digit indicating the number of mines bordering it (including diagonals). The mines (x) don't appear anymore. Mines and positions that do not border any mines both appear as empty cells (.).
Input
Line 1 : an integer w for the width of the grid.
Line 2 : an integer h for the height of the grid.
Next h lines : each line of the minefield, with dots (.) or mines (x).
Output
h lines of width w showing the completed game of Minesweeper.
Constraints
1 <= w <= 30
1 <= h <= 30
Example
Input

16
9
................
................
................
................
................
....x...........
................
................
................

Output

................
................
................
................
...111..........
...1.1..........
...111..........
................
................

------------------------------



10
7
..........
.x...x...x
..x......x
.....x....
..x.x...x.
x.........
.x...x...x

111.111.11
1.211.1.2.
12.1222.2.
.2232.1122
12.2.211.1
.322221122
2.1.1.1.1.

'''
# 2-d solution with only one loop plus one for printing

def inrease_counter(the_field, h, w):
    fh = len(the_field)
    fw = len(the_field[0])
    the_field[h][w] = "x"
    if h > 0 and w > 0:
        if the_field[h-1][w-1] == "." or the_field[h-1][w-1]=="":
            the_field[h-1][w-1] = 1
        elif not the_field[h-1][w-1] == "x":
            the_field[h-1][w-1] += 1
    if h > 0:
        if the_field[h-1][w] == "." or the_field[h-1][w] == "":
            the_field[h-1][w] = 1
        elif not the_field[h - 1][w] == "x":
            the_field[h-1][w] += 1
    if w > 0:
        if the_field[h][w-1] == "." or the_field[h][w-1]=="":
            the_field[h][w-1] = 1
        elif not the_field[h][w-1] == "x":
            the_field[h][w-1] += 1
    if h > 0 and w < fw - 1:
        if the_field[h-1][w+1] == "." or the_field[h-1][w+1] == "":
            the_field[h-1][w+1] = 1
        elif not the_field[h-1][w + 1] == "x":
            the_field[h-1][w+1] += 1
    if w < fw - 1:
        if the_field[h][w+1] == "." or the_field[h][w+1]=="":
            the_field[h][w+1] = 1
        elif not the_field[h][w + 1] == "x":
            the_field[h][w+1] += 1
    if h < fh - 1:
        if the_field[h+1][w] == "." or the_field[h+1][w]=="":
            the_field[h+1][w] = 1
        elif not the_field[h+1][w] == "x":
            the_field[h+1][w] += 1
    if h < fh - 1 and w > 0:
        if the_field[h+1][w-1] == "." or the_field[h+1][w-1]=="":
            the_field[h+1][w-1] = 1
        elif not the_field[h + 1][w - 1] == "x":
            the_field[h+1][w-1] += 1
    if h < fh -1 and w < fw - 1:
        if the_field[h+1][w+1] == "." or the_field[h+1][w+1]=="":
            the_field[h+1][w+1] = 1
        elif not the_field[h + 1][w+1] == "x":
            the_field[h+1][w+1] +=1
        elif the_field[h+1][w+1]=="x":
            the_field[h+1][w+1] = "."



w = int(input())
h = int(input())
the_field = [["" for _ in range(w)] for _ in range(h) ]
for i in range(h):
    line = input()
    for y,value in enumerate(line):
        if value == "x":
            inrease_counter(the_field, i, y)
        if i > 0 and y > 0 and (the_field[i-1][y-1] == "" or the_field[i-1][y-1] == "x"):
            the_field[i-1][y-1] = "."
        if i == h-1 and (the_field[i][y] == ""or the_field[i][y] == "x"):
            the_field[i][y] = "."

for i in range(h):
    print(*[str(x) for x in the_field[i]], sep="")
