class Solution:
    def convertToTitle(self, n: int) -> str:
        #ord('A') = 65, ord('a') = 97
        ans = ""
        while n > 0:
            n -= 1
            current = n%26
            n = n//26
            ans += str(chr(65+current))
            #print(current, ans)
        return ans[::-1]