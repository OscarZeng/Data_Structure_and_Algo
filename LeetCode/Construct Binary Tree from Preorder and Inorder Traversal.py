#Given inorder and preorder, rebuild the binary tree
#We know the structure of the preorder is [root, [left_tree], [right_tree]]
#Structure for inorder is [[left_tree], root, [right_tree]]
#Hence we can locate the root location and locate where the left_tree and right_tree are
#Doing it recursively we can have:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder) == 0:
            return None
        root = TreeNode(preorder[0])
        location = inorder.index(root.val)
        root.left = self.buildTree(preorder[1:location+1], inorder[:location])
        root.right = self.buildTree(preorder[location+1:], inorder[location+1:])
        return root

