#Here we use the recursive method to solve the problem.
class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        if n == 1:
            return [0,1]
        def helper(n):
            if n == 0:
                return []
            if n == 1:
                return ["0","1"]
            previousAns = helper(n-1)
            print(previousAns)
            ans0 = []
            ans1 = []

            for i in previousAns:
                ans0.append('0'+i)
                ans1.append('1'+i)
            #To make sure we the diff won't be bigger than 1, we can simply add one increasingly and reversely
            ansStr = ans0 + ans1[::-1]
            print(ansStr)
            return ansStr
        strAns = helper(n)
        ans = []

        for j in strAns:
            ans.append(int(j,2))
        return ans