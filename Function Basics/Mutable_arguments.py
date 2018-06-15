# This example defines the mutable objects set as argument defaults to function
# And its implications and workaround


def add_element(n, a=[]):  # A is set as mutable object, here a list !

    a.append(n)
    print(a)


# Output will accumulate the argument passed to it on subsequent calls to function.
add_element(10)
add_element(20)
add_element(30)


def add_element_safely(n, a=None):  # Following way of defining function will prevent this issue
    if a is None:
        a = []
    a.append(n)
    print(a)


# Output will not accumulate the argument passed to it on subsequent calls to function.
add_element_safely(10)
add_element_safely(20)
add_element_safely(30)
