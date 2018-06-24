#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the permutationEquation function below.
def permutationEquation(p):
    # result = []
    # for i in range(1,max(p)+1):
    #     ix = p.index(i)+1
    #     iy = p.index(ix)+1
    #     result.append(iy)
    # return result

    return [(p.index(p.index(i)+1)+1) for i in range(1, max(p)+1)]

if __name__ == '__main__':
    n = int(input())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)

    print(result)
