class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        if len(s) == 0:
            return True
        checkedS = {}
        checkedT = {}
        for i in range(len(s)):
            if s[i] not in checkedS and t[i] not in checkedT:
                checkedS[s[i]] = t[i]
                checkedT[t[i]] = s[i]
            elif (s[i] not in checkedS) != (t[i] not in checkedT):
                return False
            else:
                if checkedS[s[i]] != t[i] or checkedT[t[i]] != s[i]:
                    return False

        return True