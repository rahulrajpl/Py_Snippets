#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulDays function below.
def beautifulDays(i, j, k):
    n = 0
    for day in range(i, j+1):
        # a = list(str(day))
        # a.reverse()
        # a = int(''.join(a))
        if abs(int(str(day)[::-1]) - day) % k == 0:
            n += 1
    return n

if __name__ == '__main__':

    ijk = input().split()

    i = int(ijk[0])

    j = int(ijk[1])

    k = int(ijk[2])

    result = beautifulDays(i, j, k)

    print(result)
