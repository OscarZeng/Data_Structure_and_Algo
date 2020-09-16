#Own solution based on the algo of subsets
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if nums == []:
            return [[]]
        nums.sort()
        ans = []
        first = nums.pop()
        Thesubsets = self.subsetsWithDup(nums)
        for i in Thesubsets:
            temp = i+[first]
            if temp in Thesubsets:
                continue
            else:
                ans.append(temp)
        ans = ans + Thesubsets
        return ans
#Other solution using the backtracking
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        #Ususally when dealing with the duplicate problems, sorting will make all the same numbers together within O(NlogN) 
        nums.sort()
        #Here we can see the helper is doing the job, the meaning is generating all the subsets with duplicates.
        def helper(idx, tmp):
            res.append(tmp)
            for i in range(idx, n):
                #Here is generating, So whenever the duplicates appears, we need to skip to avoid duplicates
                if i > idx and nums[i] == nums[i-1]:
                    continue
                #Here the helper will take care the subsets given the first few elements
                helper(i+1, tmp + [nums[i]])
        helper(0, [])
        return res

作者：powcai
链接：https://leetcode-cn.com/problems/subsets-ii/solution/hui-su-suan-fa-by-powcai-6/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。