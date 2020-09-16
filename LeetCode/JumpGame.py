#The greedy algo solution which is in O(N)
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        rightMost = 0
        #Here we apply the greedy algo 
        #By keep updating the furtherest point to reach.
        for i in range(len(nums)):
            if i<= rightMost:
                rightMost = max(rightMost,i+nums[i])
                if rightMost >= len(nums) -1:
                    return True
        return False

#Own solution using the recursive method that exceed the time limits
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 0:
            return False
        if len(nums) == 1:
            return True
        if nums[0]>= len(nums) - 1:
            return True
        else:
            #ans = False
            for i in range(nums[0],0,-1):
                #ans = ans or 
                if self.canJump(nums[i:]):
                    return True
            return False