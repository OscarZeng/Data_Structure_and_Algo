class Solution:
    def convertChar(self, Charin):
        if Charin == '0':
            return 0
        if Charin == '1':
            return 1
        if Charin == '2':
            return 2
        if Charin == '3':
            return 3
        if Charin == '4':
            return 4
        if Charin == '5':
            return 5
        if Charin == '6':
            return 6
        if Charin == '7':
            return 7
        if Charin == '8':
            return 8
        if Charin == '9':
            return 9
    def multiply(self, num1: str, num2: str) -> str:
        num1Converted, num2Converted = 0,0
        for i in num1:
            current1 = self.convertChar(i)
            num1Converted = num1Converted*10 + current1
        for j in num2:
            current2 = self.convertChar(j)
            num2Converted = num2Converted*10 + current2
        ans = num1Converted * num2Converted

        return str(ans)