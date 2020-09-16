
#
# Complete the 'countMatches' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING_ARRAY grid1
#  2. STRING_ARRAY grid2
#

def countMatches(grid1, grid2):
    m,n = len(grid1), len(grid1[0])
    checked = [[False]* n for _ in range(m)]
    ans = 0

    def checkRegion(i,j):
        isMatched = True
        stack = [(i,j)]
        while len(stack) != 0:
            #print(stack,checked)
            index = stack.pop()
            currI = index[0]
            currJ = index[1]
            if checked[currI][currJ] == True:
                continue
            else:    
                checked[currI][currJ] = True
            if currI != 0 :
                if grid1[currI-1][currJ] != grid2[currI-1][currJ]:
                    isMatched = False
                if grid1[currI-1][currJ] == 1:
                    stack.append((currI-1,currJ))
            if currI != m-1 :
                if grid1[currI+1][currJ] != grid2[currI+1][currJ]:
                    isMatched = False
                if grid1[currI+1][currJ] == 1:
                    stack.append((currI+1,currJ))
            if currJ != 0 :
                if grid1[currI][currJ-1] != grid2[currI][currJ-1]:
                    isMatched = False
                if grid1[currI][currJ-1] == 1:
                    stack.append((currI,currJ-1))
            if currJ != n-1 :
                if grid1[currI][currJ+1] != grid2[currI][currJ+1]:
                    isMatched = False
                if grid1[currI][currJ+1] == 1:
                    stack.append((currI,currJ+1))
        return isMatched
    
    for i in range(m):
        for j in range(n):
            if checked[i][j] == True or grid1[i][j] == 0:
                continue
            else:
                if checkRegion(i,j) == True:
                    print(i,j, checked)
                    ans += 1
    return ans 

grid1 = [[0,0,0],[0,1,0],[1,1,1]]
grid2 = [[1,0,0],[0,1,0],[1,1,1]]
ans = countMatches(grid1,grid2)
print (ans)
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     grid1_count = int(input().strip())

#     grid1 = []

#     for _ in range(grid1_count):
#         grid1_item = input()
#         grid1.append(grid1_item)

#     grid2_count = int(input().strip())

#     grid2 = []

#     for _ in range(grid2_count):
#         grid2_item = input()
#         grid2.append(grid2_item)

#     result = countMatches(grid1, grid2)

#     fptr.write(str(result) + '\n')

#     fptr.close()
