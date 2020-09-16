class Solution:
    def __init__(self):
        pass
    def generateMatrix(self, n: int):
        #Remember to consider the three special cases
        if n==0:
            return []
        if n== 1:
            return [[1]]    
        #for margin records the four points of a matrix
        left, right, up, down = 0, n-1, 0,n-1
        #When generating 2D array, we can 
        ans = [[0]*n for i in range(n)]
        #divide the code into four steps 
        currentVal = 1   
        while(left<right) and (up < down):
            #step1: move from left to right in up
            for a in range(left, right):
                ans[up][a] = currentVal 
                currentVal += 1
                print(ans)
            
            #step2: move from up to down
            for b in range(up, down):
                ans[b][right] = currentVal
                currentVal += 1
                print(ans)
            
            #step3: move from right to left
            for c in range(right, left,-1):
                ans[down][c] = currentVal
                currentVal += 1
                print(ans)

            #step4: move from down to up
            for d in range(down, up, -1):
                ans[d][left] = currentVal
                currentVal += 1
                print(ans)
            
            left += 1
            right -= 1
            up += 1
            down -= 1

        #Consider other special cases, where the remaining middle point, remaining line and column
        if left == right and up == down:
            ans[left][up] = currentVal
        elif left == right:
            for b in range(up, down+1):
                ans[b][right] = currentVal
                currentVal += 1
        elif up == down:
            for a in range(left, right+1):
                ans[up][a] = currentVal
                currentVal += 1
        return ans


a = Solution()
n = 3
print(a.generateMatrix(n))