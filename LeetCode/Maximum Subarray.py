class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        tempSum, ansMax = nums[0], nums[0]
        for i in range(1,len(nums)):
            #Check whether previous max tempSum is useful
            #Whenever satisfy the following condition, means the previous sum is less than 0
            tempSum = max(nums[i], tempSum+nums[i])
            #Check whether the current spanSum is greater than the overall max
            ansMax = max(tempSum, ansMax)
        return ansMax