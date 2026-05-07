'''
A student is taking a coding final exam. The exam has 16 questions. The student attempts questions one by one and does not proceed until the current question is passed. Each question passed gives 6 points, except the final 16th question which gives 10 points.

Calculate the score based on the attempts provided.
Input
Line 1: An integer N for the number of attempts the student made.
Next N lines: A word attempt either PASS or FAIL
Output
score based on the attempts provided.
Constraints
1 ≤ N ≤ 100
0 ≤ score ≤ 100
Example
Input

7
PASS
PASS
PASS
PASS
PASS
PASS
PASS

Output

42
------------------------------------------
5
PASS
FAIL
PASS
PASS
PASS

24
------------------------------------------
2
FAIL
FAIL

0
------------------------------------------
16
PASS
PASS
PASS
PASS
PASS
PASS
PASS
PASS
PASS
PASS
PASS
PASS
PASS
PASS
PASS
PASS

100
------------------------------------------
17
FAIL
FAIL
FAIL
FAIL
FAIL
FAIL
FAIL
FAIL
FAIL
FAIL
FAIL
FAIL
FAIL
FAIL
FAIL
FAIL
PASS

6
------------------------------------------
32
PASS
FAIL
PASS
FAIL
PASS
FAIL
PASS
FAIL
PASS
FAIL
PASS
FAIL
PASS
FAIL
PASS
FAIL
PASS
FAIL
PASS
FAIL
PASS
FAIL
PASS
FAIL
PASS
FAIL
PASS
FAIL
PASS
FAIL
FAIL
PASS

100
------------------------------------------

'''

n = int(input())
the_total = 0 
for i in range(n):
    attempt = input()
    if attempt == "PASS":
        the_total += 6
    if i+1 == 16 and attempt == "PASS":
        the_total += 4

print(the_total)