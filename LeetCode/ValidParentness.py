#We apply the stack object hence we know that every open bracket will be closed if it is valid
class Solution:
    def checkMatch(self, s1, s2) -> bool: 
        return (s1=='(') and (s2 == ')') or  (s1=='[') and (s2 == ']') or (s1=='{') and (s2 == '}') 
    def isValid(self, s: str) -> bool:
        if s == "":
            return True
        stack = [] 
        for i in s:
            if len(stack)== 0 or (not self.checkMatch(stack[-1], i)):
                stack.append(i)
            elif self.checkMatch(stack[-1], i):
                stack.pop(-1)
        return True if len(stack)==0 else False