class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 
        if len(nums) == 1:
            return nums[0]
        ans = nums[0]
        currentMax, currentMin = nums[0], nums[0]
        for i in range(1,len(nums)):
            preMax = currentMax
            preMin = currentMin
            #Since there are both negative and positive numbers, we need to consider both cases
            #For negatigve numbers, we want it to be as smallest as possible so when we multiple by negative numbers that will be the biggest
            #It's quite clever to maintain both the smallest and biggest number since these two can convert each other.
            currentMax = max(preMax*nums[i], nums[i], preMin*nums[i])
            currentMin = min(preMax*nums[i], nums[i], preMin*nums[i])
            ans = max(ans, currentMax)
    
        return ans