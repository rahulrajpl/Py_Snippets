"""
Python Generators are powerful tool for creating iterators. They are like
regular functions, but yield statement is used to return the data.
Only last returned data is stored. So this is memory efficient than using other methods
"""


def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]


# for char in reverse('golf'):
#     print(char)

it = iter(reverse("Golf"))
print(list(x for x in reverse(("Golf"))))

# Compacting above code for reversing the string
# data = 'Golf'
# print(list(data[i] for i in range(len(data)-1, -1, -1)))
