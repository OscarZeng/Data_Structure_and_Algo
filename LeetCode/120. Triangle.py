class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        #Here we also apply the dynamic programming skill to dynamicly record the minimal sum at each path
        ansTri = [[0]*i for i in range(1,len(triangle)+1)]
        #print(ansTri)
        #Set the inital point
        ansTri[0][0] = triangle[0][0]
        for i in range(1, len(ansTri)):
            #The beginning and ending number has only one choice
            ansTri[i][0] = ansTri[i-1][0] + triangle[i][0]
            ansTri[i][-1] = ansTri[i-1][-1] + triangle[i][-1]
            for j in range(1, len(ansTri[i])-1):
                ansTri[i][j] = min(ansTri[i-1][j-1], ansTri[i-1][j]) + triangle[i][j]
        #print(ansTri)
        return min(ansTri[-1])