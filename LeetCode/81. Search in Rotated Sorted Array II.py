class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if len(nums) == 0:
            return False
        if len(nums) == 1:
            return nums[0] == target
        left, right = 0, len(nums)-1
        
        while left < right:
            if nums[left] == target or nums[right] == target:
                return True
            mid = (left + right)//2
            if mid == left:
                return False
            if nums[mid] == target:
                return True
            #When the left element duplicates, simply ignore the element
            #Here we can not use while to remove all the element since the index may overmoved to for left side
            if nums[left] == nums[mid]:
                left += 1
            elif nums[mid] == nums[right]:
                right -= 1
            #Means the pivot is in right side
            #Means the left side is order increasingly
            elif nums[left] < nums[mid]:
                if nums[left] < target < nums[mid]:
                    right = mid 
                else:
                    left = mid 
                
            else:
                if nums[mid] < target < nums[right]:
                    left = mid 
                else:
                    right = mid 
        
        return False