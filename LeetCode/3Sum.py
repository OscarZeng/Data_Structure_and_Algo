#3Sum, two pointers and fixed index 
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        ans = []
        nums.sort()
        if nums[0] > 0 or nums[-1]< 0:
            return []
        for i in range(len(nums)-2):
            if i>0 and nums[i] == nums[i-1]:
                continue
            if nums[i] > 0:
                return ans
            l = i + 1
            r = len(nums)-1
            while(l<r):
                if (nums[i] + nums[l] + nums[r])== 0:
                    ans.append((nums[i],nums[l],nums[r]))
                    while(l < r and nums[l]==nums[l+1]): l +=1
                    while(l < r and nums[r]==nums[r-1]): r -=1
                    l +=1
                    r -=1
                elif (nums[i] + nums[l] + nums[r])< 0:
                    l+=1
                else:
                    r-=1
            
        return ans
            