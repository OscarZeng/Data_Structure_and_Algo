class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return 0
        if target <= nums[0]:
            return 0
        elif target > nums[-1]:
            return len(nums)

        left, right = 0, len(nums)-1
        
        while left < right:
            if nums[left] == target:
                return left
            if nums[right] == target:
                return right
            if (right - left) == 1 and nums[left] < target < nums[right]:
                return right
            temp = int((right+left)/2)
            if nums[temp]==target:
                return temp
            elif nums[temp] > target:
                right = temp
            else:
                left = temp
            