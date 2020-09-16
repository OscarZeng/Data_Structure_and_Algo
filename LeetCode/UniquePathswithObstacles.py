class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid[0]), len(obstacleGrid)
        Upaths = [[0]*m for _ in range(n)]
        #The starting point has been blocked
        if obstacleGrid[0][0] == 1:
            return 0
        Upaths[0][0] = 1
        for i in range(n):
            for j in range(m):
                if ((i == 0) and (j ==0)) or obstacleGrid[i][j]==1 or (obstacleGrid[i-1][j]==1 and obstacleGrid[i][j-1]):
                    continue
                if i == 0 or obstacleGrid[i-1][j]==1:
                    Upaths[i][j] = Upaths[i][j-1]
                elif j == 0 or obstacleGrid[i][j-1]:
                    Upaths[i][j] = Upaths[i-1][j]
                else:
                    Upaths[i][j] = Upaths[i-1][j] + Upaths[i][j-1]
        return Upaths[n-1][m-1]