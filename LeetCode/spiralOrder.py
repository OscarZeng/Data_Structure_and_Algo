class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        #Remember to consider the three special cases
        if len(matrix)==0 or len(matrix[0])==0:
            return []
        if len(matrix) == 1:
            return matrix[0]    
        #for margin records the four points of a matrix
        left, right, up, down = 0, len(matrix[0])-1, 0, len(matrix)-1
        ans = []
        if len(matrix[0]) == 1:
            for b in range(up, down+1):
                ans.append(matrix[b][0])
            return ans
        #divide the code into four steps    
        while(left<right) and (up < down):
            #step1: move from left to right in up
            for a in range(left, right):
                ans.append(matrix[up][a])
            
            #step2: move from up to down
            for b in range(up, down):
                ans.append(matrix[b][right])
            
            #step3: move from right to left
            for c in range(right, left,-1):
                ans.append(matrix[down][c])

            #step4: move from down to up
            for d in range(down, up, -1):
                ans.append(matrix[d][left])
            
            left += 1
            right -= 1
            up += 1
            down -= 1

        #Consider other special cases, where the remaining middle point, remaining line and column
        if left == right and up == down:
            ans.append(matrix[left][up])
        elif left == right:
            for b in range(up, down+1):
                ans.append(matrix[b][right])
        elif up == down:
            for a in range(left, right+1):
                ans.append(matrix[up][a])
        return ans
            