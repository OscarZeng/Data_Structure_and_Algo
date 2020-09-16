class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums) < 3:
            return None
        nums.sort()
        ans = 9999
        for i in range(len(nums)):
            front = i + 1
            back = len(nums)-1
            thisTarget = target - nums[i]
            while front<back:
                dif = nums[front]+nums[back]-thisTarget
                if abs(dif) < abs(ans - target):
                    ans = nums[front]+nums[back]+nums[i]
                if dif == 0:
                    return target
                elif dif > 0:
                    back -= 1
                else:
                    front += 1
        return ans