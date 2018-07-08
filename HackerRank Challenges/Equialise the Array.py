#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the equalizeArray function below.
def equalizeArray(arr):
    # c = [0] * len(arr)
    # for i in arr:
    #     c[i+1] += 1
    # return len(arr)-max(c)
    c = []
    for i in set(arr):
        c.append(arr.count(i))
    return len(arr)-max(c)


if __name__ == '__main__':
    n = 5
    arr = list(map(int, "3 3 2 1 3".rstrip().split()))
    result = equalizeArray(arr)
    print(result)
