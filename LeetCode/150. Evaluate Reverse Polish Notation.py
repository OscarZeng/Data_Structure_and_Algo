class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            #print(stack, i)
            if i in "+-*/":
                num1 = stack.pop()
                num2 = stack.pop()
                #Here we need to take care the order of the numbers
                stack.append( self.calculate(num2, num1,i))
            else:
                stack.append(int(i))
        return stack[0]
        

    def calculate(self,num1, num2, operator):
        if operator == '+':
            return num1 + num2
        if operator == '-':
            return num1 - num2
        if operator == '*':
            return num1 * num2
        if operator == '/':
            return int(num1 / num2)