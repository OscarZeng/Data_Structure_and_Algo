#This use the property of mutable object of list,
#Which means when we pass the list to the function, we are actuall passing the referrence of the mutable object
#Here we just need to consider three conditions that makes a valid parenthesis
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def GPDFS (left, right, S):
            if len(S) == 2*n:
                ans.append("".join(S))
                return
            if left < n:
                S.append('(')
                GPDFS(left+1, right, S)
                S.pop()
            if right < left:
                S.append(')')
                GPDFS(left, right+1, S)
                S.pop()
        
        GPDFS(0,0,[])
        return ans