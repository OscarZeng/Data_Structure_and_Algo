class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        isMax = True
        for i in range(len(nums)-1):
            #Starting from the back to front
            reverseIndex = len(nums) - i - 1
            if nums[reverseIndex] > nums[reverseIndex-1]:
                isMax = False
                for k in range(len(nums)- reverseIndex):
                    #Starting from the back check which one is bigger than reverseIndex -1 
                    rIndex = len(nums) - k -1 
                    if nums[rIndex] > nums[reverseIndex-1]:
                        nums[rIndex], nums[reverseIndex-1] =  nums[reverseIndex-1],  nums[rIndex]
                        #Here nums[reverseIndex:].reverse() is not working
                        nums[reverseIndex:] = nums[reverseIndex:][::-1]
                        return
        if isMax:
            #nums = nums[::-1] is not working
            # nums[:]= nums[::-1] is working
            nums.reverse()
            return 