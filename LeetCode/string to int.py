class Solution:
    def __init__(self):
        pass
    def myAtoi(self, s: str) -> int:
        #Preprocess the string, only the first element considered
        ss = s.strip().split(' ')[0]
        #Check whether only white space
        if ss == "":
            return 0
        toConvert = ""
        #Check whether the first char is signeed or not an integer.
        if '0' <= ss[0] <= '9' or ss[0] == '-' or ss[0] == '+':
            toConvert += ss[0]
        else:
            return 0
        
        for i in ss[1:]:
            if '0' <= i <= '9':
                toConvert += i
            else:
                break
        if toConvert == "-" or toConvert == "+":
            return 0
        convertedNum = int(toConvert)
        if convertedNum >= (2**31 - 1):
            return (2**31-1)
        elif convertedNum <= (-2**31):
            return (-2**31)
        else:
            return convertedNum

s = "199 qoido 2123 12 312802hhbkajbdqjln"
TSolution = Solution()
print(TSolution.myAtoi(s))