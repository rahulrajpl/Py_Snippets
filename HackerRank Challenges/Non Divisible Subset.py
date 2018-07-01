#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the nonDivisibleSubset function below.
def nonDivisibleSubset(k, S):
    c = []
    # print("Original Array:", S)
    remainder_array = [i % k for i in S]
    # print("Reminder Array:", remainder_array)
    check_array = []
    for i in set(remainder_array):
        if k-i not in check_array:
            check_array.append(i)
    # print("Check Array: ", check_array)
    # for i in check_array:
    #     if i==0 or i*2==k:
    #         c.append(1)
    #         continue
    #     c.append(max(remainder_array.count(i), remainder_array.count(k-i)))
    #
    # print("Final Array:", c)
    return sum([1 if i==0 or i*2==k else max(remainder_array.count(i), remainder_array.count(k-i)) for i in check_array])


if __name__ == '__main__':
    # nk = input().split()
    # nk = "10 4".split()
    # nk = "5 5".split()
    # nk = "4 3".split()
    nk = "10 13".split()

    n = int(nk[0])

    k = int(nk[1])

    # S = list(map(int, input().rstrip().split()))
    # S = list(map(int, "1 2 3 4 5 6 7 8 9 10".rstrip().split()))
    # S = list(map(int, "2 7 12 17 22".rstrip().split()))
    # S = list(map(int, "1 7 2 4".rstrip().split()))
    S = list(map(int, "2375782 21836421 2139842193 2138723 23816 21836219 2948784 43864923 283648327 23874673".rstrip().split()))

    result = nonDivisibleSubset(k, S)

    print(result)