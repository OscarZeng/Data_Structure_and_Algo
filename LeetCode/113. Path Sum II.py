# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, Sum: int) -> List[List[int]]:
        if root == None:
            return []
        ans = []
        #Here we use the path(list) to store the path
        #Since list is immutable object, when we pass the list to the function, we are passing the referrence
        def findSum(node, currentSum, path):
            currentSum -= node.val
            path.append(node.val)
            if node.left == None and node.right == None:
                if currentSum == 0:
                    ans.append(path.copy())
                    #Hence we shall remember to pop the latest added element
                    path.pop()
                    return 
            if node.left != None:
                findSum(node.left, currentSum, path)
            if node.right != None:
                findSum(node.right, currentSum, path)
            path.pop()
        findSum(root, Sum, [])
        return ans