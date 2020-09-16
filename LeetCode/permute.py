class Solution:
    def  __init__(self):
        pass
    def permute(self, nums):
        if len(nums) == 1:
            return [nums]
        ans = []
        #Here we use the recursion. 
        #Attach each element to the permmute of the rest of the element
        for i in nums:
            currentNums = nums.copy()
            currentNums.remove(i)
            #Recursion doesn't have to be at the end
            permuteNums = self.permute(currentNums)
            for j in permuteNums:
                ans.append([i]+j)
        return ans

if __name__ == '__main__':
    s = Solution()
    n = 6
    nums = []
    for i in range(n):
        nums.append(str(i+1))
    print("nums:", nums)
    ans = s.permute(nums)
    # print("ans:", ans)
    for j in ans:
        print(j)