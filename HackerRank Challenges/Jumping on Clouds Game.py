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
    jumps = 0
    try:
        while i != l:
            if c[i+2] == 1:
                jumps += 1
                i = i+1
                continue
            elif c[i+2] == 0:
                jumps += 1
                i = i+2
                continue
    except:
        pass
    return jumps


if __name__ == '__main__':
    # n = int(input())
    n = 6

    # c = list(map(int, input().rstrip().split()))
    c = list(map(int, "0 0 0 0 1 0".rstrip().split()))

    result = jumpingOnClouds(c)

    print(result)