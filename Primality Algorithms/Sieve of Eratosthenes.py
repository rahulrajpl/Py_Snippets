"""
Sieve of Eratosthenes

Primality Checks for all Numbers upto n
Computes an finite sequence of primes using simple generators
"""
from math import sqrt
import time


def primes_up_to(n):
    """Generates all primes less than n."""
    try:
        if n < 16:
            return
        F = [True] * n
        seq1 = range(3, int(sqrt(n)), 2)
        seq2 = range(seq1[-1] + 2, n, 2)
        for p in filter(F.__getitem__, seq1):
            yield p
            for q in range(p * p, n, 2 * p):
                F[q] = False
        for p in filter(F.__getitem__, seq2):
            yield p
    except Exception:
        pass


t1 = time.time()
for i in primes_up_to(1000): # Print all prime numbers less than 1000
    print(i)
t2 = time.time()

