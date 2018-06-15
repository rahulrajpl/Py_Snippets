"""
set function is used to generate an iterable with unique elements out of another iterable
"""

a = [1,2,3,4,5,4,3,2,1]
print([i for i in set(a)]) # This will print only unique elements