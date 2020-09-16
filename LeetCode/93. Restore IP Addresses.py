class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) < 4 or len(s) > 12:
            return []
        baseNum, extra = len(s)//4, len(s)%4
        ans = []
        print(baseNum)
        #Here I am also using the helper function inside to generate the all possible combinations the ans
        def helper(remainString, remainNums, usedNums):
            #When either four digits used up or the string used up, end
            if remainString == "" or remainNums == 0:
                #Only when both of them are used up fits the requirement
                if remainNums == 0 and remainString == "":
                    ans.append('.'.join(usedNums))
                return
            #The first number is only one digi
            usedNums.append(remainString[0])
            helper(remainString[1:],remainNums-1,usedNums)
            usedNums.pop() 
            #The first number has two digits, here the first digit can't be zero
            if  len(remainString) >= 2 and remainString[0] != '0':
                usedNums.append(remainString[:2])
                helper(remainString[2:],remainNums-1,usedNums)
                usedNums.pop()
            #The first number has three digits, additionally the first number must be smaller than 256
            if  len(remainString) >= 3 and remainString[0] != '0' and int(remainString[:3]) < 256:
                usedNums.append(remainString[:3])
                helper(remainString[3:],remainNums-1,usedNums)
                usedNums.pop()
        
        helper(s,4,[])
        return ans