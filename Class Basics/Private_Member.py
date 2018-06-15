class Mapping:
    """
    Concept of Private members in Class implemetation in Python

    Private members do not exists in its true sense in Python

    Name Mangling is implemented to avoid name conflicts during inheritance

    """
    def __init__(self, iterable):
        self. item_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.item_list.append(item)

    __update = update # Private copy of the function update

class MappingSubClass(Mapping):
    def update(self, keys, values):
        # Provide a new signature to function update
        # but does not break __init__()
        for item in zip(keys, values):
            self.item_list.append(item)

if __name__ == '__main__':
    a = MappingSubClass([1,2,3])
    a.update([1],[2])
    print(a.item_list)

    b = Mapping([1,2,3])
    print(b.item_list)
    # Private method can still be accessed
    # Convention is _ClassName__PrivateMethodName(args)
    print(b._Mapping__update([4])) # still able to access the 'private member'
    # Such name manglings are used mostly to avoid accidents while inheritance implementation


