class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        ans = [False] * len(s)
        ans[0] = True
        #For some of the problem, we don't have to be too smart in the beginning
        #Solve the problem first and then improve the algorithm
        for i in range(len(s)):
            if ans[i] == False:
                continue
            for word in wordDict:
                if len(word) > len(s[i:]):
                    continue
                if word == s[i:] and ans[i] == True:
                    return True
                if s[i:i+len(word)] == word:
                    ans[i+ len(word)] = True
            
        return False