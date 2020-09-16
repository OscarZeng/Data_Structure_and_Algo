# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if root == None:
            return 0
        #Here we can not use ans as an integer to pass its referrence
        def addNum(root, currNums):
            currNums = currNums + str(root.val)
            if root.left == None and root.right == None:
                return int(currNums)
            ans = 0
            if root.left != None:
                ans += addNum(root.left, currNums)
            if root.right != None:
                ans += addNum(root.right, currNums)
            return ans
            
        return addNum(root, "")
            