'''
You must output the reverse of the Fibonacci function.
Fib(X) = Y
With Fib(1) = Fib(2) = 1
And Fib(N) = Fib(N - 1) + Fib(N - 2)
Input
Long Integer Y
Output
Integer X
Constraints
0 < X < 2^16
0 < Y < 2^64
Example
Input

13

Output

7

---------------------
 Test 2

 233

 13
 ---------------------
 3
 Test 3

 46368

 24
 ---------------------
 Test 4

 12586269025

 50

'''
y = int(input())

the_sequence = [1,1]
the_step = 2
if y < 2:
        print(1)
else:
    while not y == the_sequence[-1]:
        temp = the_sequence[-1] + the_sequence[-2]
        the_sequence.append(temp)
        the_step += 1
    else:
        print(the_step)
