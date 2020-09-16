"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        #Always remember to consider the base case, which may not fit in the logic downside
        if root == None:
            return root
        #Firstly Store the nodes in BFSorder with the record which level you are in
        BFSOrder = []
        queue = [(root,1)]
        while len(queue) != 0:
            current = queue.pop(0)
            currentNode = current[0]
            currentLevel = current[1]
            BFSOrder.append((currentNode, currentLevel))
            if currentNode.left != None:
                queue.append((currentNode.left, currentLevel+1))
                queue.append((currentNode.right, currentLevel+1))
        #print(BFSOrder)
        #Given the order to connect the tree
        for nodeTupleIdx in range(len(BFSOrder)-1):
            if BFSOrder[nodeTupleIdx][1] == BFSOrder[nodeTupleIdx+1][1]:
                BFSOrder[nodeTupleIdx][0].next = BFSOrder[nodeTupleIdx+1][0]
            else:
                BFSOrder[nodeTupleIdx][0].next = None
        BFSOrder[-1][0].next = None
        return root 

