"""
Performing Breadth First Search BFS
Also called Level Order Search
"""


class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data


class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def levelOrder(self, root):
        #  Implementation of Breadth First Search
        level_order = list()
        bsf_queue = list()
        bsf_queue.append(root)
        while len(bsf_queue) != 0:
            current = bsf_queue[0]
            if current is not None:
                level_order.append(current.data)
            bsf_queue.remove(bsf_queue[0])
            try:
                for next_node in [current.left, current.right]:
                    if next_node not in bsf_queue:
                        current = next_node
                        bsf_queue.append(current)
            except Exception:
                continue

        for i in level_order:
            print(i, end=" ")


T = int(input())
myTree = Solution()
root = None
for i in range(T):
    data = int(input())
    root = myTree.insert(root, data)
myTree.levelOrder(root)
