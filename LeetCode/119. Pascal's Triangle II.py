class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        rowIndex += 1
        if rowIndex == 0:
            return []
        if rowIndex == 1:
            return [1]
        if rowIndex == 2:
            return [1,1]
        
        ans = [[1],[1,1]]
        for i in range(2, rowIndex):
            line = [1]
            for j in range(1, i):
                line.append(ans[i-1][j-1]+ans[i-1][j])
            line.append(1)
            ans.append(line)
        
        return ans[-1]