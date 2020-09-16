class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if len(candidates) == 0:
            return []
        #Sort the list in decreasing order
        #1. we can filter out too big numbers
        #2. we can avoid repitition by only check the element afterwards
        candidates.sort(reverse=True)
        ans = []
        for i in range(len(candidates)):
            if candidates[i] > target:
                continue
            elif candidates[i] == target:
                ans.append([candidates[i]])
            else:
                subTarget = target - candidates[i]
                #by checking candidates[i:], we can avoid same result
                subCombinationSum = self.combinationSum(candidates[i:], subTarget)
                for j in subCombinationSum:
                    ans.append([candidates[i]]+j)
        return ans

