# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if len(nums) == 0:
            return None
        if len(nums) == 1:
            return TreeNode(nums[0])
        midIdx = len(nums)//2
        midVal = nums[midIdx]
        root = TreeNode(midVal)
        root.left = self.sortedArrayToBST(nums[:midIdx])
        root.right = self.sortedArrayToBST(nums[midIdx+1:])
        return root