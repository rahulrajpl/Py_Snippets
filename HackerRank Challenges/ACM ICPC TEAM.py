#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import combinations


# Complete the acmTeam function below.
def acmTeam(topic):
    c = combinations(topic, 2)
    k = []
    for i in list(c):
        t1 = int(i[0],2)
        t2 = int(i[1],2)
        t3 = list(str(bin(t1|t2)[2:])).count('1')
        k.append(t3)
    return max(k), k.count(max(k))
if __name__ == '__main__':
    nm = "4 5".split()

    n = int(nm[0])

    m = int(nm[1])

    topic = ["10101", "11100", "11010", "00101"]

    # for _ in range(n):
    #     topic_item = input()
    #     topic.append(topic_item)

    result = acmTeam(topic)
    print(result)
