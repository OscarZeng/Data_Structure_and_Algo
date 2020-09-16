# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        def inOrder(root):
            if root == None:
                return 
            inOrder(root.left)
            ans.append(root.val)
            inOrder(root.right)

        inOrder(root)
        return ans