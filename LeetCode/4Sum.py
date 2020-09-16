class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 4:
            return []
        ans = []
        nums.sort()
        if 4*nums[0] > target or 4*nums[-1]< target:
            return []
        for k in range(len(nums)-3):
            if k>0 and nums[k] == nums[k-1]:
                continue
            if 4*nums[k] > target:
                return ans
            for i in range(k+1, len(nums)-2):
                if i>k+1 and nums[i] == nums[i-1]:
                    continue
                if 3*nums[i] + nums[k]  > target:
                    break
                l = i + 1
                r = len(nums)-1
                while(l<r):
                    if (nums[k]+nums[i] + nums[l] + nums[r])== target:
                        ans.append((nums[k] ,nums[i],nums[l],nums[r]))
                        while(l < r and nums[l]==nums[l+1]): l +=1
                        while(l < r and nums[r]==nums[r-1]): r -=1
                        l +=1
                        r -=1
                    elif (nums[k]+nums[i] + nums[l] + nums[r])< target:
                        l+=1
                    else:
                        r-=1
            
        return ans
            