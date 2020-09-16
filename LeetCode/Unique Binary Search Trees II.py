# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0:
            return []
        def generateUniqueTrees(left, right):
            #The reason we have this condition
            #is that we need to complete the tree by adding the None to the leaves of the tree
            if left > right:
                return [None]

            ans = []
            #generate different trees including left and right
            for i in range(left, right+1):
                #Generate all the possible trees in left
                leftAns = generateUniqueTrees(left, i-1)
                #Generate all the possible trees in righ
t                rightAns = generateUniqueTrees(i+1, right)
            
                for l in leftAns:
                    for r in rightAns:
                        root = TreeNode(i)
                        root.left = l
                        root.right = r
                        ans.append(root)
            return ans
            
        return generateUniqueTrees(1,n)