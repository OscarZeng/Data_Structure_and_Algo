#Own Solution: By simply check whether the combination already exist
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
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
                if [candidates[i]] not in ans:
                    ans.append([candidates[i]])
                #When target equals to the smallest candidate, break
                # if candidates[i] == candidates[-1]:
                #     break
            else:
                subTarget = target - candidates[i]
                #by checking candidates[i:], we can avoid same result
                subCombinationSum = self.combinationSum2(candidates[i+1:], subTarget)
                for j in subCombinationSum:
                    if [candidates[i]]+j not in ans:
                        ans.append([candidates[i]]+j)
        return ans

#Own Solution: Here we know the repitition will happen when the adjacent element has been check repeatly
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if len(candidates) == 0:
            return []
        #Sort the list in decreasing order
        #1. we can filter out too big numbers
        #2. we can avoid repitition by only check the element afterwards
        candidates.sort(reverse=True)
        ans = []
        for i in range(len(candidates)):
            if i>0 and candidates[i] == candidates[i-1]:
                continue
            if candidates[i] > target:
                continue
            elif candidates[i] == target:
                #if [candidates[i]] not in ans:
                ans.append([candidates[i]])
                #When target equals to the smallest candidate, break
            else:
                subTarget = target - candidates[i]
                #by checking candidates[i:], we can avoid same result
                subCombinationSum = self.combinationSum2(candidates[i+1:], subTarget)
                for j in subCombinationSum:
                    ans.append([candidates[i]]+j)
        return ans

#Others Solution, use the similar method in generate parentness
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates or not target:
            return []
        candidates.sort()
        self.res = []
        self.generateC(candidates, target, 0, [])
        return self.res 
    #Use the helper function to positively reach out every possible combination 
    def generateC(self, candidates, target, idx, unit):
        if target == 0:
            self.res.append(unit[:])
            return 
        
        for i in range(idx, len(candidates)):
            if target - candidates[i] < 0: # pruning 
                break 
            if i > idx and candidates[i] == candidates[i-1]: # 去重
                continue 
            unit.append(candidates[i])
            self.generateC(candidates, target - candidates[i], i+1, unit)
            unit.pop()