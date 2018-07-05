#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    i = 0
    l = len(c)
    jumps = -1
    while i<l:
        if i < l-2 and c[i+2] == 0: i += 1
        jumps += 1
        i += 1

    return jumps

if __name__ == '__main__':
    # n = int(input())
    n = 6

    # c = list(map(int, input().rstrip().split()))
    c = list(map(int, "0 0 0 1 0 0".rstrip().split()))

    result = jumpingOnClouds(c)

    print(result)