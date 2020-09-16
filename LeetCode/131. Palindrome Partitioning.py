class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        def allPalindromes(currList, remainStr):
            #print(currList, remainStr)
            if len(remainStr)==0:
                #When we are using the inner recursion to get all the condition.
                #If the element to be add is a mutable object(usually a list), remember to do the copy other wise it will refer to the same object.
                ans.append(currList.copy())
                return
            for i in range(1,len(remainStr)+1):
                if remainStr[:i] == remainStr[:i][::-1]:
                    currList.append(remainStr[:i])
                    allPalindromes(currList, remainStr[i:])
                    currList.pop()
        allPalindromes([],s)
        return ans


#Test cases: "aab", "ajkniarfaioencoajdsnc[a", "", "aaaaa"
#1 pass