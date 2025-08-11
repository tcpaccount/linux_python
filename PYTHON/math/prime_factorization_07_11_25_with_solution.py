"""
Every number has a unique prime factorisation.
https://www.mathsisfun.com/prime-factorization.html

Example
12 = 2×2×3

2310 = 2×3×5×7×11

For a given input number, your program must output the sum of the numbers in the unique prime factorisation of that number.
Input
Line 1: An integer N greater than 1
Output
1 line The sum of the prime factors of N
Constraints
1<N<15000
Example
Input

60

Output

12

----------
11

11
--------------
1086

186
------------
13230

30

"""


def is_prime(nmbr):
    # try to understand why we can only check up until sq root of the number + 1
    # meaning no need to loop through whole seq 2 .. nmbr
    for i in range(2, int(nmbr ** 0.5) + 1):
        if not nmbr % i:
            return False
    return True

def add_prime(prime_list):
    start_number = known_prime_numbers[-1] + 1
    while not is_prime(start_number):
        start_number += 1
    known_prime_numbers.append(start_number)

result_list = []
# we don't know ahead of time how long seq of primes we'll need
# but let's start with only one, i.e. number 2 and add more if needed
known_prime_numbers = [2,]
n = int(input())


while not n == 1:
    for prime_number in known_prime_numbers:
        if not n % prime_number:
            result_list.append(prime_number)
            n //=prime_number
            break
    else:
        add_prime(known_prime_numbers)


print(sum(result_list))
