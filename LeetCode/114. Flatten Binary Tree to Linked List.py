# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        #Firstly we do the preorder 
        nodeInPre = []
        def preOrder(root):
            if root == None:
                return
            nodeInPre.append(root.val)
            preOrder(root.left)
            preOrder(root.right)
        preOrder(root)
        print(nodeInPre)

        #Recreate the tree
        preNode = root
        for nodeIdx in range(1,len(nodeInPre)):
            node = TreeNode(nodeInPre[nodeIdx])
            preNode.right = node
            preNode.left = None
            preNode = node
