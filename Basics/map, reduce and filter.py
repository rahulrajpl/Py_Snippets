import math
from functools import reduce


def area(r):
    return math.pi * r*r


radius = [1,2,3,4,5]

# How to compute the area of list of radius
# Method 1: Direct Method
a = []
for i in radius:
    a.append(area(i))
print(a)

# Method 2: Using Map Function
a = []
print(list(map(area, radius)))

# How to filter area greater than particular value
a = list(map(area, radius))
print(list(filter(lambda x: x > 25, a)))

# How to add sum of all radius in the list above
# Method 1: Direct method using for loop.
sum = 0
for i in radius:
    sum = sum + i
print(sum)

# Method 2: Using reduce function.
print(reduce(lambda x, y: x+y, radius))
