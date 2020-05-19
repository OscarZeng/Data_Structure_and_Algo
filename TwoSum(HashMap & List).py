#Using the hashmap to save the time for searching the index
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diction = {}
        #Set the dict[num] = index, so we can save the time doing search
        for i,num in enumerate(nums):
            if diction.get(target - num) != None:
                return diction[target - num], i
            diction[num] = i
            

#Using the list, just go through the list once
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
        	#Check whether the target nums[i] is in the rest of the list
            if (target- nums[i]) in nums[i+1:]:
                return i, nums.index(target - nums[i], i+1)