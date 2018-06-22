"""
To find one of eight possible 3X3 magic square if set of 9 numbers are given between [0 9]
"""

def createMagicSquare(a):
    a.sort()
    magic_number = int(sum(a) / 3)
    b = [None] * len(a)
    pivot = a[4]
    b[4] = pivot
    b[0], b[2], b[6], b[8] = pivot + 1, pivot + 3, pivot - 3, pivot - 1
    b[1], b[3] = magic_number - (b[0] + b[2]), magic_number - (b[0] + b[6])
    b[5], b[7] = magic_number - (b[3] + b[4]), magic_number - (b[6] + b[8])
    return b

def displayMagicSquare(b):
    s = [b[i:i+3] for i in range(0, len(b), 3)]
    for item in s:
        print(item)


def isMagicSquare(b):
    magic_number = int(sum(b)/3)
    for row in [b[i:i + 3] for i in range(0, len(b), 3)]:
        if sum(row) != magic_number:
            return False
    for i in range(3):
        if sum([b[i] for i in range(0, len(b), 3)]) != magic_number:
            return False
    if sum([b[i] for i in range(0, len(b), 4)]) != magic_number:
        return False
    return True



#a = list(map(int, input().strip().split(' ')))
a = [1,2,3,4,5,6,7,8,9]

b = createMagicSquare(a)
displayMagicSquare(b)
print(isMagicSquare(b))
