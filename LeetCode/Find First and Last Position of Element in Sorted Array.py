class Solution:
    def expandRegion(self, index, nums):
        target = nums[index]
        leftIndex, rightIndex = index, index
        #Here we need to make sure index is in range 
        while leftIndex>=0 and  nums[leftIndex] == target:
            leftIndex -= 1
        while rightIndex< len(nums) and nums[rightIndex] == target:
            rightIndex += 1
        return [leftIndex+1, rightIndex-1]

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        #Usually no element and only one element shall be considered specifically
        if len(nums) == 0:
            return [-1,-1]
        if len(nums) == 1:
            return [0,0] if nums[0] == target else [-1,-1]

        left ,right = 0, len(nums)-1
        #Here we can just check the first and last element only once 
        if nums[left] == target:
            return self.expandRegion(left, nums)
        if nums[right] == target:
            return self.expandRegion(right, nums)
        while left < right:
            mid = int((left+right)/2)
            #Means the interval has already closed
            if mid == left:
                return [-1,-1]
            if nums[mid] == target:
                return self.expandRegion(mid,nums)
            elif target > nums[mid]:
                left = mid
            else:
                right = mid
