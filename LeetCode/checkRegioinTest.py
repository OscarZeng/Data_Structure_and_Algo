def checkRegion(grid,gridC):
	count = 0
	m,n = len(grid), len(grid[0])
	checked = [[0]*n for _ in range(m)]

	def DFS(i,j):
		isMatched = True
		stack = [(i,j)]
		while len(stack) != 0:
			index = stack.pop()
			currI = index[0]
			currJ = index[1]
			#Always remember to check whether the node has been checked before, if not we may end in infinite loop
			if checked[currI][currJ] == 1:
				continue
			else:
				checked[currI][currJ] = 1
			if currI != 0:
				if grid[currI-1][currJ] != gridC[currI-1][currJ]:
					isMatched = False
				if grid[currI-1][currJ] == 1:
					stack.append((currI-1,currJ))
			if currI != m-1:
				if grid[currI+1][currJ] != gridC[currI+1][currJ]:
					isMatched = False
				if grid[currI+1][currJ] == 1:
					stack.append((currI+1,currJ))
			if currJ != 0:
				if grid[currI][currJ-1] != gridC[currI][currJ-1]:
					isMatched = False
				if grid[currI][currJ-1] == 1:
					stack.append((currI,currJ-1))
			if currJ != n-1:
				if grid[currI][currJ+1] != gridC[currI][currJ+1]:
					isMatched = False
				if grid[currI][currJ+1] == 1:
					stack.append((currI,currJ+1))
		return isMatched

	for i in range(m):
		for j in range(n):
			if checked[i][j] == 1 or grid[i][j] == 0:
				continue
			else:
				print(i,j)
				if DFS(i,j) == True:
					count += 1
				print(checked)
				
	return count




grid1 = [[0,0,0,0,0,0,1],
		[0,1,0,1,1,1,0],
		[1,1,1,0,1,0,1],
		[1,1,1,0,1,1,1],
		[1,1,1,0,0,0,0]]
grid2 = [[0,0,0,0,0,0,1],
		[0,1,1,1,1,0,0],
		[1,1,1,0,1,0,1],
		[1,1,1,0,1,1,1],
		[1,1,1,0,0,0,0]]
print(checkRegion(grid1,grid2))