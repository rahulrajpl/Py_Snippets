#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the pickingNumbers function below.
def pickingNumbers(a):
    # Solution 1

    # sublist_lengths = []
    # for i in set(a):
    #     sublist_length = a.count(i) + a.count(i+1)
    #     sublist_lengths.append(sublist_length)
    # return max(sublist_lengths)

    # Solution 2
    return max([a.count(i)+a.count(i+1) for i in set(a)])



if __name__ == '__main__':

    # n = int(input())
    n = 6
    # a = list(map(int, input().rstrip().split()))
    a = [1, 2, 2, 3, 1, 2]

    result = pickingNumbers(a)

    print(result)
