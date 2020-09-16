#Own solution using dynamic programming which exceeds the timelimit
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        #Remove dummy * since multiple * together is meaningless
        while p.find("**") != -1:
            p = p.replace("**", "*")
            #print(p)
        #This dictionary will record all the existing matches
        dp = {}
        def helper(s, p):    
            #print(s, p, len(s), len(p))
            if len(p) == 0 and len(s) != 0:
                dp[(s,p)] = False
                return False
            if len(s) == 0 and len(p) != 0:
                if p[0] != '*':
                    dp[(s,p)] = False
                    return False
            if s == p:
                dp[(s,p)] = True
                return True
            elif p[0] == '*':
                ans = False
                #When you don't know what to be sure, try some very simple examples
                for i in range(len(s)+1 - (len(p[1:])+1)//2):
                    if dp.get((s[i:], p[1:])) == True:
                        dp[(s,p)] = True
                        return True
                    ans = ans or helper(s[i:], p[1:])
                dp[(s,p)] = ans
                return ans
            elif p[0] == '?' or p[0] == s[0]:
                if dp.get((s[1:],p[1:])) != None:
                    dp[(s,p)] = dp.get((s[1:],p[1:]))
                    return dp[(s,p)]
                else: 
                    dp[(s,p)] = helper(s[1:], p[1:])
                    return dp[(s,p)]
            dp[(s,p)] = False
            return False
        helper(s,p)
        return dp[(s,p)]

#Sample solution using dynamic programming, O(mn) where m and n indicates len of s and p respectively
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        while p.find("**") != -1:
            p = p.replace("**", "*")
        m, n = len(s), len(p)

        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True
        for i in range(1, n + 1):
            if p[i - 1] == '*':
                dp[0][i] = True
            else:
                break
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 1] | dp[i - 1][j]
                elif p[j - 1] == '?' or s[i - 1] == p[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                
        return dp[m][n]

#Sample solution using greedy algorithm
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def allStars(st: str, left: int, right: int) -> bool:
            return all(st[i] == '*' for i in range(left, right))
        
        def charMatch(u: str, v: str) -> bool:
            return u == v or v == '?'

        sRight, pRight = len(s), len(p)
        while sRight > 0 and pRight > 0 and p[pRight - 1] != '*':
            if charMatch(s[sRight - 1], p[pRight - 1]):
                sRight -= 1
                pRight -= 1
            else:
                return False
        
        if pRight == 0:
            return sRight == 0
        
        sIndex, pIndex = 0, 0
        sRecord, pRecord = -1, -1
        while sIndex < sRight and pIndex < pRight:
            if p[pIndex] == '*':
                pIndex += 1
                sRecord, pRecord = sIndex, pIndex
            elif charMatch(s[sIndex], p[pIndex]):
                sIndex += 1
                pIndex += 1
            elif sRecord != -1 and sRecord + 1 < sRight:
                sRecord += 1
                sIndex, pIndex = sRecord, pRecord
            else:
                return False

        return allStars(p, pIndex, pRight)
