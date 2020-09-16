class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if nums == []:
            return [[]]
        ans = []
        first = nums.pop()
        Thesubsets = self.subsets(nums)
        for i in Thesubsets:
            ans.append(i+[first])
        ans = ans + Thesubsets
        return ans