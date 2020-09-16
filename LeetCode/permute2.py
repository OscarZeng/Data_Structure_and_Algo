#Own Solution: Using dic to check whether the element already used
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        ans = []
        # Here we can use dictionary to check whether the ans exists
        checkAns = {}
        for i in nums:
            currentNums = nums.copy()
            currentNums.remove(i)
            permuteNums = self.permuteUnique(currentNums)
            for j in permuteNums:
                temp = [i]+j
                #Here we check whether the permutation exists
                if checkAns.get(str(temp)) == True:
                    #temp in ans:
                    continue
                else:
                    ans.append(temp)
                    checkAns[str(temp)] = True

        return ans

# Use dict to track how many times the element can exist
# Similar structure to the generate parentness
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        dic = {}
        for i in nums:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        res = []
        def backtrack(dic, path):
            if len(path) == len(nums):
                res.append(path[:])

            for i in dic.keys():
                if dic[i] == 0:
                    continue
                dic[i] -= 1
                path.append(i)
                backtrack(dic, path)
                path.pop()
                dic[i] += 1

        backtrack(dic,[])
        return res

作者：bai-ban-2
链接：https://leetcode-cn.com/problems/permutations-ii/solution/hui-su-li-yong-kong-jian-huan-qu-shi-jian-by-bai-b/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。