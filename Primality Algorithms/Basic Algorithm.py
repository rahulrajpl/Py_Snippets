"""
Basic Algorithm

 If a number is divisable by another number less or equal to the square root of the first number...
 it is NOT prime. So Time Complexity is O(sqrt(n)).
 Remember that the number 1 is not prime.
"""

from math import sqrt


def is_prime(n):
    if n == 1:
        return "Not prime"
    sq = int(sqrt(n))
    for x in range(2, sq+1):
        if n % x == 0:
            return "Not prime"
    return "Prime"


T = int(input())
test_cases = []
for i in range(T):
    test_cases.append(int(input()))

for t in test_cases:
    print(is_prime(t))
