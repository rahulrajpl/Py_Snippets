from functools import reduce
n = [0,1,2,3,4,5,6,7,8,9]
m = reduce(lambda x,y:x+y or x,n)

print(n)
print(m)

sum = 0
for i in n:
    sum += i

print(sum)