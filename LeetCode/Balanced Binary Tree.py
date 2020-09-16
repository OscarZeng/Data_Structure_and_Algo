# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def treeHeight(self, root):
        if root == None:
            return -1
        #Use the recursive method to calculate the height
        return 1 + max(self.treeHeight(root.left), self.treeHeight(root.right))

    def isBalanced(self, root: TreeNode) -> bool:
        if root == None:
            return True
        #Only this root and all of its subtrees are balanced can be called balanced
        if (abs(self.treeHeight(root.left) - self.treeHeight(root.right))<=1):
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        else:
            return False