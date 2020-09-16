class Solution:
    def isHappy(self, n: int) -> bool:
        #Always consider base cases as usual
        if n == 0:
            return False
        if n == 1:
            return True
        #Here we need to pay attention that the loop may not end with
        #Original value, hence we better record each value to make sure that there must be no loop.
        seen = {}
        while True:
            newN = 0
            for i in str(n):
                newN += int(i)**2
            print(newN, n)
            if newN == 1:
                return True
            if seen.get(newN) == True:
                return False
            seen[newN] = True
            n = newN