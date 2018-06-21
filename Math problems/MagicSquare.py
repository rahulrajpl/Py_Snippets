"""
To find the 3X3 magic square if set of 9 numbers are given between [0 9]
"""

#a = list(map(int, input().strip().split(' ')))
a = [1,2,3,4,5,6,7,8,9]
a.sort()
magic_number = int(sum(a) / 3)

b = [None] * len(a)
pivot = a[len(a)//2]
b[4] = pivot
b[0], b[8] = pivot+1, pivot-1
b[2], b[6] = pivot+3, pivot-3
b[1], b[3] = 15 - (b[0] + b[2]), 15 - (b[0] + b[6])
b[5], b[7] = 15 - (b[3] + b[4]), 15 - (b[6] + b[8])


i = 0
while i < len(b):
    for _ in range(3):
        print(b[i], end=' ')
        i += 1
    print()
