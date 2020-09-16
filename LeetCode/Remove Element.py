class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ans =  len(nums) - nums.count(val)
        index = 0
        while index < len(nums):
            if nums[index] == val:
                nums.pop(index)
                continue
            index += 1
        return ans