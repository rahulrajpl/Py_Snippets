#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    # Single line solution with list comprehension
    # return sum([ar.count(x)//2 for x in set(ar)])
    pairs = 0
    for x in set(ar):
        pairs += math.floor(ar.count(x)/2)
    return pairs



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
