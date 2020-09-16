class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m ,n =  len(matrix[0]), len(matrix)
        zerosIdx = []
        #Mark all the zeroes' index
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    zerosIdx.append((i,j))
        
        #Use the dictionary to record them
        zerosDictRow = {}
        zerosDictColumn = {}
        for a,b in zerosIdx:
            zerosDictRow[a] = 1
            zerosDictColumn[b] = 1
        
        #Check the Dict and make them zeroes
        for i in range(n):
            for j in range(m):
                if zerosDictRow.get(i) == 1 or zerosDictColumn.get(j) == 1:
                    matrix[i][j] = 0
