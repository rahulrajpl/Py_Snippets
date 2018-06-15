#  Finally, the least frequently used option is to specify that a function can be called with an arbitrary number
#  of arguments. These arguments will be wrapped up in a tuple (see Tuples and Sequences). Before the
#  variable number of arguments, zero or more normal arguments may occur.


def arbitrary_fun(*args):
    print(args)


if __name__ == '__main__':
    arbitrary_fun(1,2,3,4,5)
    arbitrary_fun('hello','world','this','is','a','test')
