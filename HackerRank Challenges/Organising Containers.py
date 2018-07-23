#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the organizingContainers function below.
def organizingContainers(container):
    container_total = []
    ball_total = []
    j = 0
    for c in container:
        container_total.append(sum(c))
        i = 0
        s = 0
        while i < len(container):
            s += container[i][j]
            i += 1
        ball_total.append(s)
        j += 1
    container_total.sort()
    ball_total.sort()
    if container_total == ball_total:
        print("Possible")


if __name__ == '__main__':

    q = 2

    for q_itr in range(q):
        n = int(input())

        container = []

        for _ in range(n):
            container.append(list(map(int, input().rstrip().split())))

        result = organizingContainers(container)

        print(result)
