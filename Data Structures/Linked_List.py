class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class Solution:
    def display(self, head):
        current = head
        while current:
            print(current.data, end=' ')
            current = current.next

    def insert(self, head, data):
        new_node = Node(data)
        cur = head
        if cur is None:
            head = new_node
            return head
        else:
            while cur.next is not None:
                cur = cur.next
            cur.next = new_node
        return head


my_list = Solution()
T = int(input())
head = None
for i in range(T):
    data = int(input())
    head = my_list.insert(head, data)
my_list.display(head);