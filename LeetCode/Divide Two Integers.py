# The point here is exponentially increase the divisor.
# Linearly increase is way too much slow
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        ans, isMinus = 0, False
        if dividend < 0:
            isMinus = not isMinus
        if divisor < 0:
            isMinus = not isMinus
        dividend, divisor = abs(dividend), abs(divisor)
        if divisor == 1:
            ans = dividend
        else:
            ans = self.recursiveDiv(dividend, divisor)
        if isMinus:
            ans = ans*(-1)
        return ans if ((-1)*2**31<=ans<=2**31-1) else (2**31-1)
    #here we use the recursive way to implement the binary search    
    def recursiveDiv(self,dividend, divisor):
        originalDivisor = divisor
        if dividend< divisor:
            return 0
        if dividend == divisor:
            return 1
        ans = 1
        while(dividend > divisor):
            divisor += divisor
            ans += ans
        ans = ans/2
        dividend = dividend - divisor/2
        ans += self.recursiveDiv( dividend, originalDivisor)
        return int(ans)
            
