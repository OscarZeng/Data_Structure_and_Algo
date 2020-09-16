# Own solution using list of strings
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        dp = [""] * numRows
        index = 0
        adding = True
        if numRows == 1:
            return s
        for i in s:
            if index == 0:
                adding = True
            if index == numRows-1:
                adding = False
            dp[index] += i 
            if adding:
                index += 1
            else:
                index -= 1
        ans = ""
        for a in dp:
            ans += str(a)
        
        return ans
