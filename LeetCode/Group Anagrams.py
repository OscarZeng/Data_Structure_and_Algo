class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dicAns = {}
        ans = []
        #Use the dictionary to record the ans 
        for s in strs:
            temp = "".join(sorted(s))
            if dicAns.get(temp):
                dicAns[temp].append(s)
            else:
                dicAns[temp] = [s]
        #Then forword it to a list
        for l in dicAns.values():
            ans.append(l)
        return ans