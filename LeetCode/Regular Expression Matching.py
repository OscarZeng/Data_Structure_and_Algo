class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if p == "":
            return not s        
        thisMatch = bool(s) and (p[0] == s[0] or p[0] == '.')
        if len(p)>=2 and  p[1] == '*':
            return (thisMatch and self.isMatch(s[1:], p)) or self.isMatch(s, p[2:])
        else:
            return thisMatch and self.isMatch(s[1:], p[1:])