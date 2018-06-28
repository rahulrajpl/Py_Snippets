#!/bin/python3

import math
import os
import random
import re
import sys

CUTS_APPEND = cuts.append(len(arr))


def cutTheSticks(arr):
    cuts = []
    # cut_length = min(arr)
    # while len(arr):
    #     cut_length = min(arr)
    #     cuts.append(len(arr))
    #     arr = list(map(lambda x:x-cut_length, arr))
    #     arr = list(filter(lambda j:j!=0, arr))
    # return cuts
    while arr:
        cuts.append(len(arr))
        arr = [a for a in arr if a!=min(arr)]
    return cuts


if __name__ == '__main__':
    n = 8

    arr = list(map(int, "1 2 3 4 3 3 2 1".rstrip().split()))

    result = cutTheSticks(arr)
    print(result)