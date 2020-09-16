class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        elif n == 2:
            return '11'
        else:
            count = 1
            res = ''
            #Here the recursion doesn't have to be at the end
            #Simply follow the logic and do the recursion
            s = self.countAndSay(n - 1)
            #Simply implement the logic here shall be fine
            for i in range(1, len(s)):
                if s[i] == s[i - 1]:
                    count += 1
                else:
                    res = res + str(count) + s[i - 1]
                    count = 1
            res = res + str(count) + s[i]
            return res