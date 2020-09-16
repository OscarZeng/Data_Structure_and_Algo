class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        ans = 0
        
        primes = [True] * n
        for a in range(2, n):
            if primes[a-1]:
                for j in range(a+a, n, a):
                    primes[j-1] = False
                #print(primes)
        for i in range(2,n):
            if primes[i]:
                ans += 1
        return ans

