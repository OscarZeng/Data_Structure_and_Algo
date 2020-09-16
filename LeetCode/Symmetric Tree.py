# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isMirror(self, leftNode, rightNode):
        if leftNode == None and rightNode == None:
            return True
        if leftNode== None or rightNode ==None:
            return False 
        if leftNode.val != rightNode.val:
            return False
        return self.isMirror(leftNode.right, rightNode.left) and self.isMirror(leftNode.left, rightNode.right) 
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.isMirror(root.left,root.right) if root else True

        