class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid[0]), len(grid)
        minSumPath = [[-1]*m for _ in range(n)]
        minSumPath[0][0] = grid[0][0]
        #The first line shall be just sum
        for i in range(1,m):
            minSumPath[0][i] = grid[0][i] + minSumPath[0][i-1]
        #This first row shall also be just sum
        for j in range(1,n):
            minSumPath[j][0] = grid[j][0] + minSumPath[j-1][0]

        for a in range(1,m):
            for b in range(1,n):
                minSumPath[b][a] = grid[b][a] + min(minSumPath[b-1][a], minSumPath[b][a-1])
        return minSumPath[-1][-1]