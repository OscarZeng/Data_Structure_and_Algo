class Solution:
    def numTrees(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        nums = [0] * (n+1)
        #Store the nums in array for dynamic programming
        nums[0], nums[1] = 1,1
        for i in range(2, n+1):
            #For each node can be the root
            for j in range(i+1):
                #The total numbers can be the nums of left possibles times the nums of right possibles
                leftNums = nums[j-1]
                rightNums = nums[i-j]
                #Sum them for each node to be the root
                nums[i] += leftNums * rightNums
        
        return nums[-1]