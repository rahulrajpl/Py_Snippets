#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):
    energy = 100  # initial energy
    i = k % n  # initial jump from 0
    energy -= c[i] * 2 + 1  # initial energy loss
    while i != 0:
        i = (i + k) % n
        energy -= c[i] * 2 + 1
    return energy

nk = "8 2".split()
n = int(nk[0])
k = int(nk[1])
c = list(map(int, "0 0 1 0 0 1 1 0".rstrip().split()))
result = jumpingOnClouds(c, k)
print(result)

