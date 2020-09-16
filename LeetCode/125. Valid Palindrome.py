class Solution:
    def isPalindrome(self, s: str) -> bool:
        lowerS = s.strip().lower()
        finalS = ""
        for i in lowerS:
            if 'a' <= i <= 'z' or '0'<=  i <= '9':
                finalS += i
        return finalS == finalS[::-1]