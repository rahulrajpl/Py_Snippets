#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the saveThePrisoner function below.
def saveThePrisoner(n, m, s):
    # i = m + s - 1
    # if i > n:
    #     if i%n == 0:
    #         return n
    #     return i%n
    # return i
    return (n if (m + s - 1) % n == 0 else (m + s - 1) % n) if (m + s - 1) > n else (m + s - 1)

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        nms = input().split()

        n = int(nms[0])

        m = int(nms[1])

        s = int(nms[2])

        result = saveThePrisoner(n, m, s)

        print(result)