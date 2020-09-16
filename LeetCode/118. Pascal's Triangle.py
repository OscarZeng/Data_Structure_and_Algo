class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1],[1,1]]
        
        ans = [[1],[1,1]]
        for i in range(2, numRows):
            line = [1]
            for j in range(1, i):
                line.append(ans[i-1][j-1]+ans[i-1][j])
            line.append(1)
            ans.append(line)
        
        return ans