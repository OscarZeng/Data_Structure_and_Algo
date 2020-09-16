class Solution:
    def reverseParentheses(self, s: str) -> str:
        if len(s) == 0:
            return ""
        #Here we use a stack to store the locations of open parentness
        stack = []
        i = 0
        while(i<len(s)):
            if s[i] == '(':
                #Store the location of the open parentness
                stack.append(i)
            
            if s[i] == ')':
                #Find the open parentness
                lastOpen = stack.pop()
                s = s[:lastOpen] + s[lastOpen+1:i][::-1] + s[i+1:]
                print(s)
                i = i-2
            i += 1
        return s
            