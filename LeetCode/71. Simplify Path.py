class Solution:
    def simplifyPath(self, path: str) -> str:
        #Remove the begining / and split the /
        pathList = path.strip('/').split('/')
        #Use the stack to store the path
        stack = []
        for i in pathList:
            #Whenever encounter the .., pop the stack
            if i == "..":
                if len(stack) > 0:
                    stack.pop()
            #Ignore these
            elif i == '' or i == '.':
                continue
            else:
                stack.append(i)
        #Remember to reformulate the entire string
        return '/'+ '/'.join(stack)
