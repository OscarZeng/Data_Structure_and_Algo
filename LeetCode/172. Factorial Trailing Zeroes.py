class Solution:
    def trailingZeroes(self, n: int) -> int:
        #As we can notice, there are more than enough 2s in n! with limited 5s
        #Hence we just need to take care of the 5
        ans = 0
        while n > 0:
            n = n//5
            ans += n

        return ans