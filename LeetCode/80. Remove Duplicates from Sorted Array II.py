class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)
        index = 2
        while index< len(nums):
            if nums[index-2] == nums[index-1] and nums[index-1] == nums[index]:
                nums.pop(index)
                continue
            index += 1
        return len(nums)

