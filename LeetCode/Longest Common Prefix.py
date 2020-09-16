#Longest Common Prefix, Own solution
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        anslen = len(strs[0])
        for s in strs[1:]:
            if len(s)< anslen:
                anslen = len(s)
            while(anslen>0):
                if s[:anslen] == strs[0][:anslen]:
                    break
                else: anslen -= 1
            if anslen == 0:
                return ""
        return strs[0][:anslen]