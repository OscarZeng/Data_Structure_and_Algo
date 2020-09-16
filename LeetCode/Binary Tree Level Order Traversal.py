# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        ans = [[]]
        if root == None:
            return []
        #Here we have another arguement that records the level of each node.
        def levelOrderEach(root, level):
            #Stop when reach the leaves
            if root== None:
                return
            #When reaching a new level, add a new line
            if level > len(ans):
                ans.append([])
            #traversal the tree by preorder, so we can add one by one
            ans[level-1].append(root.val)
            levelOrderEach(root.left, level+1)
            levelOrderEach(root.right, level+1)
        
        levelOrderEach(root, 1)
        return ans
