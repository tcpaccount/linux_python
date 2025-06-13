'''
You are given the letters of a sentence that are scattered in a square grid at different vertical heights, but are placed in the correct left-to-right order by column.
Your task is to "catch" the letters and print the sentence on a single line by reading column-by-column.
If there isn't any letter in a column, consider it as a white space ' '.
Input
Line 1:h - the height (and width) of the square grid.
Next h Lines: grid - A square grid of h x h characters representing the grid.
Output
Line 1: sentence - The sentence formed by catching one letter from each column (left to right).
Constraints
1 ≤ h ≤ 100
The grid is always square: height = width = h
Each column contains at most one letter (or none).
Example
Input
10
      u

  t
       m

        p.
C
   s
 a   j

Output
Cats jump.
---------------
34

                            n   e
                               s .

                              i


                      t




           t              s
       w
                        e    r


         d                 u

                   r
             a
            e
S       e      b       h

  e               o
                 f
    br
                    e




                e
 h    e
She brewed tea before the sunrise.

---------------
30
             h
                      e

         n
      b             o
 t

    s     k    n             .




                          o s

  a
                           k

                     n

       l
   r              o

        i
                         o
              e  n
                        l
            w
S


Stars blink when no one looks.

---------------
30



         a

     o
                          t

                             .
  r        c    n

        d         t        o

                   h     f
                        o
   o           o


                       o    p


                      r
A
                    e
          n
    b
            e

      t      d

A robot danced on the rooftop.
---------------



'''

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

h = int(input())
result = [" " for _ in range(h)]
for i in range(h):
    row = input()
    for index, y in enumerate(row):
        if not y == " ":
            result[index] = y

print("".join(result))