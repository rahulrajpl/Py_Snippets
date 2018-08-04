#!/bin/python3

from math import sqrt
import os
import random
import re
import sys

# Complete the kaprekar Numbers function below.
def kaprekarNumbers(p, q):

    # for i in [x for x in range(p,q+1) if x not in range(2,4)]:
    #     s = str(i*i)
    #     if i == 1 or i == int(s[:int(len(s)/2)])+int(s[int((len(s)/2)):]):
    #         k.append(str(i)+' ')
    # for s in [str(x*x) for x in range(p, q+1) if x not in range(2,4)]:
    #     if sqrt(int(s)) == 1 or sqrt(int(s)) == int(s[:int(len(s)/2)])+int(s[int((len(s)/2)):]):
    #         k.append(str(int(sqrt(int(s))))+' ')

    k = ''.join(map(lambda s: str(int(sqrt(int(s))))+' '
    if sqrt(int(s)) == 1 or sqrt(int(s)) == int(s[:int(len(s)/2)])+
       int(s[int((len(s)/2)):]) else "", [str(i*i) for i in range(p, q+1) if i not in range(2,4)]))
    print("Invalid Range" if len(k) == 0 else k)


if __name__ == '__main__':
    p = 1

    q = 100

    kaprekarNumbers(p, q)