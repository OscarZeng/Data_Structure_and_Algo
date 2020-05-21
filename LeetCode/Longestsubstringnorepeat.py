
def lengthOfLongestSubstring(self, s: str) -> int:
    ans = 0
    if len(s)==1:
        return 1
    for i in range(len(s)):
        finished = True
        exist_dict = {}
        for j in range(i, len(s)):
            if exist_dict.get(s[j]):
                #ans = max(j-i, ans)
                finished = False
                break
            exist_dict[s[j]] = 1
        ans = max(j-i, ans)
        if finished: 
            return ans 
    return ans