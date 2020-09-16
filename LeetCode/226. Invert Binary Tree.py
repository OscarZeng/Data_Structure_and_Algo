# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isleaf(self, root):
        return root.left == None and root.right == None
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root == None:
            return None
        elif self.isleaf(root):
            return root
        #Switching when both nodes are leaves or one is None one is leaf
        #This is the base condition for switching
        elif (root.left == None or self.isleaf(root.left)) and (root.right == None or self.isleaf(root.right)):
            root.left, root.right = root.right, root.left
            return root
        #For the rest of the condition, we simply need to switch the left and right tree and invert the tree itself.
        else:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
            return root
