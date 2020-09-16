# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        iniMax = float(inf)
        iniMin = float(-inf)
        #When it comes to check something, usually we will use the recursion due to the structure of Binary Tree
        #Here the key point is that for any BST, the root value shall be bigger than all the value in the left and all the value in the right 
        def helper (root, Max, Min):
            #The null tree is true
            if root == None:
                return True
            if root.val >= Max or root.val <= Min:
                return False
            isLeftBST = helper(root.left, root.val, Min)
            isRightBST = helper(root.right, Max ,root.val)
            return isLeftBST and isRightBST
        
        return helper(root, iniMax, iniMin)