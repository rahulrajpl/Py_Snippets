#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kaprekarNumbers function below.
def kaprekarNumbers(p, q):
    k = []
    for i in [x for x in range(p,q+1) if x not in range(2,4)]:
        s = str(i*i)
        if i == 1 or i == int(s[:int(len(s)/2)])+int(s[int((len(s)/2)):]):
            k.append(str(i)+' ')
    k = ''.join(k)
    if len(k)>0:
        print(k)
    else:
        print("Invalid Range")


if __name__ == '__main__':
    p = 1

    q = 100

    kaprekarNumbers(p, q)