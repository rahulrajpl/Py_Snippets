"""
To find the 3X3 magic square if set of 9 numbers are given between [0 9]
"""

def createMagicSquare(a):
    a.sort()
    magic_number = int(sum(a) / 3)

    b = [None] * len(a)
    pivot = a[len(a) // 2]
    b[4] = pivot
    b[0], b[8] = pivot + 1, pivot - 1
    b[2], b[6] = pivot + 3, pivot - 3
    b[1], b[3] = magic_number - (b[0] + b[2]), magic_number - (b[0] + b[6])
    b[5], b[7] = magic_number - (b[3] + b[4]), magic_number - (b[6] + b[8])
    return b

def displayMagicSquare(b):
    col = 3 # Number of Columns in Magic Square
    s = [b[i:i+col] for i in range(0, len(b), col)]
    for item in s:
        print(item)


def isMagicSquare(b):
    pass


#a = list(map(int, input().strip().split(' ')))
a = [1,2,3,4,5,6,7,8,9]

b = createMagicSquare(a)
displayMagicSquare(b)

