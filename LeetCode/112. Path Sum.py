# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, Sum: int) -> bool:
        if root == None:
            return False
        Sum -= root.val
        #This is the condition when it reaches leaf node
        if root.left == None and root.right == None:
            return Sum == 0
        return self.hasPathSum(root.left, Sum)  or self.hasPathSum(root.right,Sum)