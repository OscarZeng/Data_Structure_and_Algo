class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return
        if len(nums) == 1:
            return nums[0]
        #Three parts are left, mid and right, mid = (left+right)//2
        left, right = 0, len(nums)-1
        while(left <= right):
            mid = (left + right)//2
            print(left, right, mid)
            print(nums[left], nums[right], nums[mid])
            #only one element here
            if left == right:
                return nums[left]
            #Only two elements here
            elif left == mid:
                return min(nums[left], nums[right])
            #case1: left < mid < right, means all the things is in order
            if nums[left] <= nums[mid] and nums[mid] <= nums[right]:
                return nums[left]
            #case2: right<left < mid, means the minimal point must at right side 
            elif nums[left] < nums[mid] and nums[right] < nums[left]:
                left = mid 
                continue
            #case3: mid < right < left, means the minimal point at left side
            elif nums[mid] < nums[right] and nums[right] < nums[left]:
                right = mid
                continue

