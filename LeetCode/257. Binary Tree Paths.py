# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if root == None:
            return []
        ans = []
        #Here we also use the helper function to do the question
        def allPaths(currentPath, root):
            if root.left == None and root.right == None:
                ans.append(currentPath)
                return
            if root.left != None:
                allPaths(currentPath + "->" + str(root.left.val), root.left)
            if root.right != None:
                allPaths(currentPath + "->" + str(root.right.val), root.right)

        allPaths(str(root.val), root)
        return ans