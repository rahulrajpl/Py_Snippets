class Dog:
    kind = 'canine'
    def __init__(self, name):
        self.name = name

if __name__ == '__main__':
    d1 = Dog('Jumpo')
    d2 = Dog('Tiger')
    # Following are Instance variable
    print(d1.name)
    print(d2.name)

    # Following are Class variable
    print(d1.kind)
    print(d2.kind)
