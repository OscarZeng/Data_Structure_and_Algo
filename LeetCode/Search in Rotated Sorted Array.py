#Need to consider a few special cases here, which are len(nums) == 1,
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #Always remember to consider the base case
        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        left, right = 0, (len(nums) - 1)
        while(left < right):
            if target == nums[left]:
                return left
            if target == nums[right]:
                return right
            #Divide into [left,mid] [mid+1, right], two parts
            mid = int((left + right)/2)
            #When the interval is only 2 and neither left nor right matches
            if left == mid:
                return -1
            if target == nums[mid]:
                return mid
            #which means pivot is in right side
            if nums[left] < nums[mid]:
                if (nums[left]<target<nums[mid]):
                    right = mid
                    continue
                else:
                    left = mid
                    continue
            #Which means pivot is in left side
            else:
                if (nums[mid]<target<nums[right]):
                    left =  mid
                    continue
                else:
                    right = mid
                    continue
            #for case [1,3] target = 2, the case where it may leads to bug

        return -1
                
