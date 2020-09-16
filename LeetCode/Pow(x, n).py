class Solution:
    def myPow(self, x: float, n: int) -> float:
        #Use the recursion to implement binary search
        if n == 0:
            return 1
        if n == 1:
            return x
        #Here we consider -1 as a special case
        if n == -1:
            return 1/x
        #convert negative number into positive number
        isNegative = False
        if n<0:
            isNegative = True
            n = (-1)*n
        #we can start directly from 2 since 0 1 -1 are considered
        ans = x*x
        powIndex = 2 
        while(powIndex*2<n):
            ans = ans*ans
            powIndex = powIndex*2
        
        ans = ans * self.myPow(x, n-powIndex)
        if isNegative:
            ans = 1/ans
        return ans