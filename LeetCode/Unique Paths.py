class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        Upaths = [[0]*m for _ in range(n)]
        #Given the starting point has one method, we can implement dynamic programming
        Upaths[0][0] = 1
        for i in range(n):
            for j in range(m):
                if (i == 0) and (j ==0):
                    continue
                if i == 0:
                    Upaths[i][j] = Upaths[i][j-1]
                elif j == 0:
                    Upaths[i][j] = Upaths[i-1][j]
                else:
                    Upaths[i][j] = Upaths[i-1][j] + Upaths[i][j-1]
        return Upaths[n-1][m-1]
                