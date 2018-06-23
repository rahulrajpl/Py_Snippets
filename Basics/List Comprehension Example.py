#!/bin/python3

import math
import os
import random
import re
import sys
from functools import reduce

# Complete the utopianTree function below.
def utopianTree(n):
    if n == 0:
        return 1
    elif n == 1:
        return 2
    else:
        h = 1
        for i in range(2,n+2):
            if i%2 == 0:
                h += h
            else:
                h += 1
        return h

if __name__ == '__main__':

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = utopianTree(n)

        print(result)
