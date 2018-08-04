#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kaprekarNumbers function below.
def kaprekarNumbers(p, q):
    k = []
    for i in range(p, q+1):
        if i == 1:
            k.append(str(i)+' ')
            continue
        if i == 2 or i == 3: continue
        s = i * i
        s = str(s)
        s1 = s[:int(len(s)/2)]
        s2 = s[int((len(s)/2)):]
        if int(s1)+int(s2) == i:
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