class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = Node()
    
    def append(self, data):
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
        elems = []
        cur_node = self.head
        while cur_node.next is not None:
            cur_node = cur_node.next
            elems.append(cur_node.data)
        print(elems)
    
    def get(self, index):
        if index >= self.length():
            print("Error: Index out of range!")
            return None
        cur_idx = 0
        cur_node = self.head
        while True:            
            if cur_idx == index:
                return cur_node.data
            cur_node = cur_node.next
            cur_idx += 1
    
    def erase(self, index):
        if index >= self.length():
            print("Error: Index out of range")
            return None
        cur_idx = 0
        cur_node = self.head
        while True:
            last_node = cur_node
            cur_node = cur_node.next
            if cur_idx is index-1:
                last_node.next = cur_node.next
                return
            cur_idx += 1
            
    
My_List = LinkedList()

My_List.display()

My_List.append(1)
My_List.append(2)
My_List.append(3)
My_List.append(4)
My_List.append(5)
My_List.display()
print("Total Elements in list are:", My_List.length())
print("Element at Index 3 is: ", My_List.get(3))
print("Erasing element at 2")
My_List.erase(2)
My_List.display()
