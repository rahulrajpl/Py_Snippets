#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the squares function below.
def squares(a, b):
    # count = 0
    # p = math.sqrt(a)
    # if p % 1 == 0: count += 1
    # while True:
    #     p = int(p) + 1
    #     i = pow(int(p), 2)
    #     if i > b: return count
    #     count += 1
    return math.floor(math.sqrt(b))-math.ceil(math.sqrt(a)) + 1


if __name__ == '__main__':
    q = int(input())
    for q_itr in range(q):
        ab = input().split()
        a = int(ab[0])
        b = int(ab[1])
        result = squares(a, b)
        print(result)


