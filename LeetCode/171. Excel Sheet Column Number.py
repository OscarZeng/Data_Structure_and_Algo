class Solution:
    def titleToNumber(self, s: str) -> int:
        #The idea here is number in 26. For zero we can consider it as nothing.
        ans = 0
        for i in s:
            num = ord(i) - ord('A') + 1
            ans = ans*26 + num
        return ans