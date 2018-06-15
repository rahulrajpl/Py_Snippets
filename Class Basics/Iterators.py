"""
Following small piece of code explains the behind the scenes of
implementation of 'for item in iterables' statement
"""

names = ['rahul','reshmi','balu','sumit']
it = iter(names)
print(it)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
try:
    print(next(it))
except:
    print("Iterables completed")
