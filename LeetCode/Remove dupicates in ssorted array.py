#Remove dupicates in ssorted array
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        while(i+1<len(nums)):
            if nums[i]  == nums[i+1]:
                nums.pop(i)
            else:
                i += 1
        return len(nums)