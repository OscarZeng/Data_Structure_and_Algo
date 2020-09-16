#Analyse the question, notice that the matrix is simply another form of sorted array
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0 or len(matrix[0])==0:
            return False

        m,n = len(matrix), len(matrix[0])
        
        left, right = 0, m*n-1
        while left <= right:
            middle = (left + right)//2
            midRow = middle // n
            midColumn = middle % n
            if matrix[midRow][midColumn] == target:
                return True
            elif matrix[midRow][midColumn] < target:
                left = middle + 1
            elif matrix[midRow][midColumn] > target:
                right = middle - 1
            
        return False