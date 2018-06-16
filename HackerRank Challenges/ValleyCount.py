#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the countingValleys function below.
def countingValleys(n, s):
    nv, v, i = 0, 0, 0
    while i < n:
        if s[i] == 'U':
            try:
                if v < 0 and v + 1 == 0:
                    nv += 1
            except Exception:
                pass
            v += 1
        if s[i] == 'D':
            v -= 1
        i += 1
    return nv


if __name__ == '__main__':

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    print(result)
