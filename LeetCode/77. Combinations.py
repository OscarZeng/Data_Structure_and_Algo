class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans, nums = [], []

        #When using the backtracking skills, first to understand the meaning of the recursive function.
        def UniqueCombination(currCombin, currNum):
            if len(currCombin) == k:
                ans.append(currCombin[:])
            for i in range(currNum, n+1):
                #Add the current number
                currCombin.append(i)
                #Add the rest of the nums
                UniqueCombination(currCombin,i+1)
                currCombin.pop()
        
        UniqueCombination([],1)
        return ans
            