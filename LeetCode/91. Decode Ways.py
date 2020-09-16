class Solution:
    def numDecodings(self, s: str) -> int:
        #Here we consider the basic conditions
        if s[0] == '0':
            return 0
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1 if int(s) != 0 else 0
        
        #Here we apply the dynamic programming
        ans = [0] * len(s)
        #The hard part it make sure that every special condition for the first two digits have been considered
        ans[-1] = 1 if int(s[-1]) != 0 else 0
        if int(s[-2]) == 0:
            ans[-2] = 0
        elif  int(s[-1]) == 0:
            if int(s[-2]) > 2:
                ans[-2] = 0
            else:
                ans[-2] = 1
        else:    
            ans[-2] = 1 if int(s[-2:]) > 26 else 2
        for i in range(len(s)-3, -1, -1):
            if int(s[i]) == 0:
                ans[i] = 0
            elif int(s[i:i+2]) <= 26:
                ans[i] = ans[i+1] + ans[i+2]
            else:
                ans[i] = ans[i+1]

        return ans[0]