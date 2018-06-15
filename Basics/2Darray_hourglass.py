#!/bin/python3

import sys

if __name__ == '__main__':
    arr = []
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    sum = -(sys.maxsize)
    for i in range(4):
        for j in range(4):
            if len(arr[i]) == len(arr[i + 2]):
                hour_glass = arr[i][j]+arr[i][j+1]+arr[i][j+2]+\
                             arr[i+1][j+1]+\
                             arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]
            sum = hour_glass if hour_glass > sum else sum

    print(sum)

