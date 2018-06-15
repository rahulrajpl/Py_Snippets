class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = Node()

    def insert(self, data):
        new_node = Node(data)
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = new_node

    def length(self):
        cur = self.head
        total = 0
        while cur.next is not None:
            total += 1
            cur = cur.next
        return total

    def display(self):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
            print(cur.data, end=' ')


ll = LinkedList()
ll.display()
ll.insert(1)
ll.insert(2)
ll.insert(3)
ll.display()
print(ll.length())